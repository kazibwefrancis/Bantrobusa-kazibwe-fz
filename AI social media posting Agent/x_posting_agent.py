"""
X Posting Agent - Main Application
"""

import logging
import time
import schedule
from datetime import datetime
from typing import Optional
from dotenv import load_dotenv

# Load environment variables FIRST before importing config
load_dotenv()

from config import validate_config, LOGGING_CONFIG
from content_manager import ContentManager
from utils import setup_logging, format_timestamp

# Setup logging
setup_logging(LOGGING_CONFIG)
logger = logging.getLogger(__name__)


class XPostingAgent:
    """Main X Posting Agent class"""
    
    def __init__(self):
        self.content_manager: Optional[ContentManager] = None
        self.is_running = False
        self._initialize()
    
    def _initialize(self) -> None:
        """Initialize the posting agent"""
        try:
            # Validate configuration
            if not validate_config():
                raise Exception("Configuration validation failed")
            
            # Initialize content manager
            self.content_manager = ContentManager()
            logger.info("X Posting Agent initialized successfully")
            
        except Exception as e:
            logger.error(f"Failed to initialize X Posting Agent: {str(e)}")
            raise
    
    def post_content(self, content: Optional[str] = None) -> bool:
        """
        Post content to X
        
        Args:
            content: Content to post, uses default if None
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            if not self.content_manager:
                logger.error("Content manager not initialized")
                return False
            
            # Use provided content or get default
            if content is None:
                content = self.content_manager.get_default_content()
            
            logger.info(f"Posting content: {content[:50]}...")
            
            # Post with retry logic
            success = self.content_manager.post_with_retry(content)
            
            if success:
                logger.info("Content posted successfully")
            else:
                logger.error("Failed to post content")
            
            return success
            
        except Exception as e:
            logger.error(f"Error posting content: {str(e)}")
            return False
    
    def post_with_media(self, content: str, media_path: str) -> bool:
        """
        Post content with media attachment
        
        Args:
            content: Content to post
            media_path: Path to media file
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            if not self.content_manager:
                logger.error("Content manager not initialized")
                return False
            
            # Upload media
            media_id = self.content_manager.upload_media(media_path)
            if not media_id:
                logger.error("Failed to upload media")
                return False
            
            # Post with media
            success = self.content_manager.post_with_retry(content, [media_id])
            
            if success:
                logger.info("Content with media posted successfully")
            else:
                logger.error("Failed to post content with media")
            
            return success
            
        except Exception as e:
            logger.error(f"Error posting content with media: {str(e)}")
            return False
    
    def schedule_posts(self) -> None:
        """Schedule automatic posts"""
        try:
            # Example scheduling - customize as needed
            schedule.every(1).hours.do(self.post_content)
            
            # You can add more scheduling rules here:
            # schedule.every().day.at("09:00").do(self.post_content, "Good morning! 🌅")
            # schedule.every().monday.at("10:00").do(self.post_content, "Monday motivation! 💪")
            
            logger.info("Post scheduling configured")
            
        except Exception as e:
            logger.error(f"Error setting up scheduling: {str(e)}")
    
    def start_scheduled_posting(self) -> None:
        """Start the scheduled posting loop"""
        try:
            self.is_running = True
            logger.info("Starting scheduled posting...")
            
            while self.is_running:
                schedule.run_pending()
                time.sleep(60)  # Check every minute
                
        except KeyboardInterrupt:
            logger.info("Stopping scheduled posting...")
            self.is_running = False
        except Exception as e:
            logger.error(f"Error in scheduled posting loop: {str(e)}")
            self.is_running = False
    
    def stop(self) -> None:
        """Stop the posting agent"""
        self.is_running = False
        logger.info("X Posting Agent stopped")
    
    def get_status(self) -> dict:
        """Get current status of the posting agent"""
        if not self.content_manager:
            return {"status": "not_initialized"}
        
        rate_limit_status = self.content_manager.get_rate_limit_status()
        
        return {
            "status": "running" if self.is_running else "stopped",
            "initialized": True,
            "rate_limits": rate_limit_status,
            "timestamp": format_timestamp()
        }


def main():
    """Main function to run the X Posting Agent"""
    try:
        logger.info("Starting X Posting Agent...")
        
        # Create agent instance
        agent = XPostingAgent()
        
        # Example usage - customize as needed
        print("X Posting Agent is ready!")
        print("Options:")
        print("1. Post once")
        print("2. Start scheduled posting")
        print("3. Check status")
        print("4. Exit")
        
        while True:
            choice = input("\nEnter your choice (1-4): ").strip()
            
            if choice == "1":
                content = input("Enter content to post (or press Enter for default): ").strip()
                if not content:
                    content = None
                
                success = agent.post_content(content)
                if success:
                    print("✅ Content posted successfully!")
                else:
                    print("❌ Failed to post content")
            
            elif choice == "2":
                agent.schedule_posts()
                print("Starting scheduled posting... Press Ctrl+C to stop")
                agent.start_scheduled_posting()
            
            elif choice == "3":
                status = agent.get_status()
                print(f"Status: {status}")
            
            elif choice == "4":
                agent.stop()
                print("Goodbye!")
                break
            
            else:
                print("Invalid choice. Please try again.")
                
    except KeyboardInterrupt:
        logger.info("Application interrupted by user")
    except Exception as e:
        logger.error(f"Application error: {str(e)}")
    finally:
        logger.info("X Posting Agent shutting down")


if __name__ == "__main__":
    main()
