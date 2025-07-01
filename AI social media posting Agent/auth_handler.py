from dotenv import load_dotenv

load_dotenv()

import tweepy
import logging
from typing import Optional
from config import API_CONFIG

logger = logging.getLogger(__name__)


class XAuthHandler:
    
    def __init__(self):
        self.api: Optional[tweepy.API] = None
        self.client: Optional[tweepy.Client] = None
        self._authenticate()
    
    def _authenticate(self) -> None:
        try:
            auth = tweepy.OAuthHandler(
                API_CONFIG['api_key'],
                API_CONFIG['api_secret']
            )
            auth.set_access_token(
                API_CONFIG['access_token'],
                API_CONFIG['access_token_secret']
            )
            
            self.api = tweepy.API(auth, wait_on_rate_limit=True)
            
            self.client = tweepy.Client(
                bearer_token=API_CONFIG['bearer_token'],
                consumer_key=API_CONFIG['api_key'],
                consumer_secret=API_CONFIG['api_secret'],
                access_token=API_CONFIG['access_token'],
                access_token_secret=API_CONFIG['access_token_secret'],
                wait_on_rate_limit=True
            )
            
            self._test_authentication()
            logger.info("Successfully authenticated with X API")
            
        except Exception as e:
            logger.error(f"Authentication failed: {str(e)}")
            raise
    
    def _test_authentication(self) -> None:
        try:
            if self.client:
                user = self.client.get_me()
                logger.info(f"Authenticated as: @{user.data.username}")
            else:
                raise Exception("Client not initialized")
        except Exception as e:
            logger.error(f"Authentication test failed: {str(e)}")
            raise
    
    def get_client(self) -> tweepy.Client:
        if not self.client:
            raise Exception("Client not authenticated")
        return self.client
    
    def get_api(self) -> tweepy.API:
        if not self.api:
            raise Exception("API not authenticated")
        return self.api
