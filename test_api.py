# Create a test file: test_api.py
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
print(f"API Key found: {bool(api_key)}")

if api_key:
    try:
        genai.configure(api_key=api_key)
        print("API configured successfully")
        
        # List available models
        print("\nAvailable models:")
        models = genai.list_models()
        for model in models:
            if 'generateContent' in model.supported_generation_methods:
                print(f"✅ {model.name}")
            else:
                print(f"❌ {model.name} (no generateContent)")
                
    except Exception as e:
        print(f"Error: {e}")
else:
    print("No API key found")