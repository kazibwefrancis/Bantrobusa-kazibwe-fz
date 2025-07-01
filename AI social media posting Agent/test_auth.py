"""
Quick test script to verify X API authentication
"""

from dotenv import load_dotenv
load_dotenv()

try:
    from auth_handler import XAuthHandler
    print("🔄 Testing X API authentication...")
    
    auth = XAuthHandler()
    print("✅ Authentication successful!")
    print("🚀 Your X Posting Agent is ready to use!")
    
except Exception as e:
    print(f"❌ Authentication failed: {str(e)}")
    print("Please check your API credentials in the .env file")
