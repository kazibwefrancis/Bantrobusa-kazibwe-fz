"""
Send a specific tweet - Edit the content below and run
"""

from dotenv import load_dotenv
load_dotenv()

from content_manager import ContentManager

# 📝 EDIT THIS LINE - Put your tweet content here:
TWEET_CONTENT = "Just deployed my X posting agent! 🤖 Time to automate my social media game. #Python #Automation #TechLife"

def main():
    print("🐦 Sending Custom Tweet...")
    print(f"📝 Content: {TWEET_CONTENT}")
    print("=" * 50)
    
    try:
        cm = ContentManager()
        success = cm.post_with_retry(TWEET_CONTENT)
        
        if success:
            print("🎉 SUCCESS! Your tweet is live!")
            print("🔗 Check your X profile to see it")
        else:
            print("❌ Failed to post - check x_posting_agent.log for details")
            
    except Exception as e:
        print(f"❌ Error: {str(e)}")

if __name__ == "__main__":
    main()
