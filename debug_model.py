import os
from dotenv import load_dotenv
from google import genai

# 1. Load your keys
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("❌ Error: GEMINI_API_KEY not found in environment.")
    exit()

print(f"🔑 Key found: {api_key[:5]}... (checking access)")

# 2. Connect directly to Google
# We use the same 'v1beta' version mentioned in your error log
try:
    client = genai.Client(api_key=api_key, http_options={'api_version':'v1beta'})
    
    print("📡 Contacting Google API to list available models...\n")
    
    # 3. List Models
    # We iterate through everything the server says you can use
    found_any = False
    for model in client.models.list():
        # We only care about models that support 'generateContent'
        if "generateContent" in model.supported_actions:
            print(f"✅ Available: {model.name}")
            found_any = True
            
    if not found_any:
        print("⚠️ No models found. Your API key might be invalid or has no access.")

except Exception as e:
    print(f"\n❌ Connection Failed: {e}")