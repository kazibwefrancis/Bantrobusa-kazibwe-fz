"""
This began as my test to see whther my keys were working but i decided to keep in the code for testing by sending tweets  without using the menu 
"""

from dotenv import load_dotenv
load_dotenv()

from content_manager import ContentManager

def send_tweet():
    """Send a tweet right now"""
    print("🐦 Quick Tweet Sender")
    print("=" * 30)
    
    # Get tweet content from user
    content = input("Enter your tweet: ").strip()
    
    if not content:
        content = "Hello from my X posting agent! 🤖 #automation"
        print(f"Using default: {content}")
    
    try:
        # Initialize and send
        cm = ContentManager()
        print("🚀 Sending tweet...")
        
        success = cm.post_with_retry(content)
        
        if success:
            print("✅ Tweet sent successfully!")
        else:
            print("❌ Failed to send tweet - check logs")
            
    except Exception as e:
        print(f"❌ Error: {str(e)}")

if __name__ == "__main__":
    send_tweet()
