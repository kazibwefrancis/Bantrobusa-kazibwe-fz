from dotenv import load_dotenv
load_dotenv()

from content_manager import ContentManager

def send_tweet():
    print("🐦 Quick Tweet Sender")
    print("=" * 30)
    
    content = input("Enter your tweet: ").strip()
    
    if not content:
        content = "Hello from my X posting agent! 🤖 #automation"
        print(f"Using default: {content}")
    
    try:
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
