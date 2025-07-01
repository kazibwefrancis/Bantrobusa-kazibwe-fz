from dotenv import load_dotenv
load_dotenv()

import tweepy
from config import API_CONFIG

def check_permissions():
    print("🔍 Checking X App Permissions...")
    print("=" * 50)
    
    try:
        client = tweepy.Client(
            bearer_token=API_CONFIG['bearer_token'],
            consumer_key=API_CONFIG['api_key'],
            consumer_secret=API_CONFIG['api_secret'],
            access_token=API_CONFIG['access_token'],
            access_token_secret=API_CONFIG['access_token_secret'],
            wait_on_rate_limit=True
        )
        
        user = client.get_me()
        print(f"✅ Authenticated as: @{user.data.username}")
        print(f"📝 User ID: {user.data.id}")
        
        print("\n🧪 Testing posting permissions...")
        
        try:
            print("⚠️  Cannot test actual posting without making a real post")
            print("   Your app likely has READ-ONLY permissions")
            
        except Exception as e:
            print(f"❌ Posting test failed: {str(e)}")
            
        print("\n" + "=" * 50)
        print("🔧 TO FIX THE POSTING ISSUE:")
        print("1. Go to: https://developer.twitter.com/en/portal/dashboard")
        print("2. Click on your app")
        print("3. Go to Settings → App permissions")
        print("4. Change from 'Read' to 'Read and Write'")
        print("5. Go to Keys and Tokens")
        print("6. Click 'Regenerate' for Access Token & Secret")
        print("7. Update your .env file with NEW tokens")
        print("8. Restart the agent")
        print("=" * 50)
        
    except Exception as e:
        print(f"❌ Error checking permissions: {str(e)}")

if __name__ == "__main__":
    check_permissions()
