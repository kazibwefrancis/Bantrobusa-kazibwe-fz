"""
Test posting with new tokens
"""

from dotenv import load_dotenv
load_dotenv()

import tweepy
from config import API_CONFIG

def test_new_tokens():
    """Test posting with the new access tokens"""
    print("🧪 Testing new access tokens...")
    print("=" * 40)
    
    try:
        # Create client with new tokens
        client = tweepy.Client(
            bearer_token=API_CONFIG['bearer_token'],
            consumer_key=API_CONFIG['api_key'],
            consumer_secret=API_CONFIG['api_secret'],
            access_token=API_CONFIG['access_token'],
            access_token_secret=API_CONFIG['access_token_secret'],
            wait_on_rate_limit=True
        )
        
        # Test authentication
        user = client.get_me()
        print(f"✅ Authenticated as: @{user.data.username}")
        
        # Test posting
        print("\n🚀 Testing tweet posting...")
        test_content = "🎉 Testing my X posting agent with new permissions! #automation #success"
        
        response = client.create_tweet(text=test_content)
        
        if response.data:
            print(f"✅ SUCCESS! Tweet posted with ID: {response.data['id']}")
            print(f"📝 Content: {test_content}")
            print("\n🎊 Your X Posting Agent is now fully functional!")
        else:
            print("❌ Failed to post tweet")
            
    except tweepy.Forbidden as e:
        print(f"❌ Still forbidden: {str(e)}")
        print("⚠️  Make sure you:")
        print("   1. Changed app permissions to 'Read and Write'")
        print("   2. Regenerated the access tokens AFTER changing permissions")
        print("   3. Updated the .env file with NEW tokens")
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")

if __name__ == "__main__":
    test_new_tokens()
