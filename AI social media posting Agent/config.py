"""
Configuration settings for the X Posting Agent
"""

import os
from typing import Dict, Any

# API Configuration
API_CONFIG = {
    'api_key': os.getenv('X_API_KEY'),
    'api_secret': os.getenv('X_API_SECRET'),
    'access_token': os.getenv('X_ACCESS_TOKEN'),
    'access_token_secret': os.getenv('X_ACCESS_TOKEN_SECRET'),
    'bearer_token': os.getenv('X_BEARER_TOKEN')
}

# Posting Configuration
POSTING_CONFIG = {
    'max_tweet_length': 280,
    'retry_attempts': 3,
    'retry_delay': 60,  # seconds
    'rate_limit_window': 900,  # 15 minutes in seconds
    'max_tweets_per_window': 300
}

# Logging Configuration
LOGGING_CONFIG = {
    'level': 'INFO',
    'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    'filename': 'x_posting_agent.log',
    'max_bytes': 10485760,  # 10MB
    'backup_count': 5
}

# Content Configuration
CONTENT_CONFIG = {
    'content_sources': [
        # Add your content sources here
        # e.g., RSS feeds, text files, databases, etc.
    ],
    'hashtags': ['#automation', '#python'],
    'default_content': [
        "Hello from my X posting agent! 🤖",
        "Automated posting is working great! 🚀",
        "Testing my Python X bot 🐍"
    ]
}

def validate_config() -> bool:
    """Validate that all required configuration is present"""
    required_keys = ['api_key', 'api_secret', 'access_token', 'access_token_secret']
    
    for key in required_keys:
        if not API_CONFIG.get(key):
            print(f"Missing required configuration: {key}")
            return False
    
    return True
