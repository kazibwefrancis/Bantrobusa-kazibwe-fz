import logging
import time
from typing import List, Optional, Dict, Any
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()

import tweepy
from auth_handler import XAuthHandler
from config import POSTING_CONFIG, CONTENT_CONFIG

logger = logging.getLogger(__name__)


class ContentManager:
    
    def __init__(self):
        self.auth_handler = XAuthHandler()
        self.client = self.auth_handler.get_client()
        self.last_post_time = None
        self.post_count = 0
        self.rate_limit_reset_time = datetime.now()
    
    def post_tweet(self, content: str, media_ids: Optional[List[str]] = None) -> bool:
        try:
            if not self._check_rate_limits():
                logger.warning("Rate limit exceeded, skipping post")
                return False
            
            if len(content) > POSTING_CONFIG['max_tweet_length']:
                logger.error(f"Tweet too long: {len(content)} characters")
                return False
            
            response = self.client.create_tweet(
                text=content,
                media_ids=media_ids
            )
            
            if response.data:
                logger.info(f"Tweet posted successfully: ID {response.data['id']}")
                self._update_rate_limit_tracking()
                return True
            else:
                logger.error("Failed to post tweet: No response data")
                return False
                
        except tweepy.TooManyRequests:
            logger.warning("Rate limit hit, waiting...")
            self._handle_rate_limit()
            return False
        except tweepy.Forbidden as e:
            error_msg = str(e)
            logger.error(f"Forbidden: {error_msg}")
            
            if "oauth1 app permissions" in error_msg.lower():
                logger.error("❌ APP PERMISSION ISSUE:")
                logger.error("   Your X app needs 'Read and Write' permissions")
                logger.error("   1. Go to: https://developer.twitter.com/en/portal/dashboard")
                logger.error("   2. Click your app → Settings → App permissions")
                logger.error("   3. Change to 'Read and Write'")
                logger.error("   4. Regenerate Access Token & Secret")
                logger.error("   5. Update your .env file with new tokens")
            
            return False
        except tweepy.BadRequest as e:
            logger.error(f"Bad request: {str(e)}")
            return False
        except Exception as e:
            logger.error(f"Unexpected error posting tweet: {str(e)}")
            return False
    
    def post_with_retry(self, content: str, media_ids: Optional[List[str]] = None) -> bool:
        for attempt in range(POSTING_CONFIG['retry_attempts']):
            if self.post_tweet(content, media_ids):
                return True
            
            if attempt < POSTING_CONFIG['retry_attempts'] - 1:
                wait_time = POSTING_CONFIG['retry_delay'] * (attempt + 1)
                logger.info(f"Retry attempt {attempt + 1} in {wait_time} seconds")
                time.sleep(wait_time)
        
        logger.error(f"Failed to post tweet after {POSTING_CONFIG['retry_attempts']} attempts")
        return False
    
    def get_default_content(self) -> str:
        import random
        content_list = CONTENT_CONFIG['default_content']
        base_content = random.choice(content_list)
        
        hashtags = CONTENT_CONFIG.get('hashtags', [])
        if hashtags:
            hashtag_str = ' ' + ' '.join(hashtags)
            if len(base_content + hashtag_str) <= POSTING_CONFIG['max_tweet_length']:
                base_content += hashtag_str
        
        return base_content
    
    def _check_rate_limits(self) -> bool:
        now = datetime.now()
        
        if now >= self.rate_limit_reset_time:
            self.post_count = 0
            self.rate_limit_reset_time = now + timedelta(seconds=POSTING_CONFIG['rate_limit_window'])
        
        if self.post_count >= POSTING_CONFIG['max_tweets_per_window']:
            return False
        
        return True
    
    def _update_rate_limit_tracking(self) -> None:
        self.post_count += 1
        self.last_post_time = datetime.now()
    
    def _handle_rate_limit(self) -> None:
        wait_time = (self.rate_limit_reset_time - datetime.now()).total_seconds()
        if wait_time > 0:
            logger.info(f"Waiting {wait_time:.0f} seconds for rate limit reset")
            time.sleep(wait_time)
    
    def upload_media(self, file_path: str) -> Optional[str]:
        try:
            api = self.auth_handler.get_api()
            media = api.media_upload(file_path)
            logger.info(f"Media uploaded successfully: ID {media.media_id}")
            return str(media.media_id)
        except Exception as e:
            logger.error(f"Failed to upload media: {str(e)}")
            return None
    
    def get_rate_limit_status(self) -> Dict[str, Any]:
        return {
            'posts_in_window': self.post_count,
            'max_posts_per_window': POSTING_CONFIG['max_tweets_per_window'],
            'window_reset_time': self.rate_limit_reset_time.isoformat(),
            'last_post_time': self.last_post_time.isoformat() if self.last_post_time else None
        }
