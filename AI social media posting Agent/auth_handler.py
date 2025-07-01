"""
X API Authentication Handler
"""

from dotenv import load_dotenv

# Load environment variables before importing config
load_dotenv()

import tweepy
import logging
from typing import Optional
from config import API_CONFIG

logger = logging.getLogger(__name__)


class XAuthHandler:
    """Handles authentication with the X API"""
    
    def __init__(self):
        self.api: Optional[tweepy.API] = None
        self.client: Optional[tweepy.Client] = None
        self._authenticate()
    
    def _authenticate(self) -> None:
        """Authenticate with X API using OAuth 1.0a and Bearer Token"""
        try:
            # OAuth 1.0a authentication for API v1.1 (if needed)
            auth = tweepy.OAuthHandler(
                API_CONFIG['api_key'],
                API_CONFIG['api_secret']
            )
            auth.set_access_token(
                API_CONFIG['access_token'],
                API_CONFIG['access_token_secret']
            )
            
            self.api = tweepy.API(auth, wait_on_rate_limit=True)
            
            # Client for API v2 (recommended)
            self.client = tweepy.Client(
                bearer_token=API_CONFIG['bearer_token'],
                consumer_key=API_CONFIG['api_key'],
                consumer_secret=API_CONFIG['api_secret'],
                access_token=API_CONFIG['access_token'],
                access_token_secret=API_CONFIG['access_token_secret'],
                wait_on_rate_limit=True
            )
            
            # Test authentication
            self._test_authentication()
            logger.info("Successfully authenticated with X API")
            
        except Exception as e:
            logger.error(f"Authentication failed: {str(e)}")
            raise
    
    def _test_authentication(self) -> None:
        """Test the authentication by making a simple API call"""
        try:
            if self.client:
                # Get current user info to test authentication
                user = self.client.get_me()
                logger.info(f"Authenticated as: @{user.data.username}")
            else:
                raise Exception("Client not initialized")
        except Exception as e:
            logger.error(f"Authentication test failed: {str(e)}")
            raise
    
    def get_client(self) -> tweepy.Client:
        """Get the authenticated Tweepy client"""
        if not self.client:
            raise Exception("Client not authenticated")
        return self.client
    
    def get_api(self) -> tweepy.API:
        """Get the authenticated Tweepy API (v1.1)"""
        if not self.api:
            raise Exception("API not authenticated")
        return self.api
