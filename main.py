import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

def verbose_checker():
    try:
          if sys.argv[2] == "--verbose":
               return 1
    except:
         return 0

def main():
        
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    client = genai.Client(api_key=api_key)
    try:
        user_prompt = sys.argv[1]
    except:
        print(f"Usage: python <prompt>")
        exit(1)
        
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)])
    ]


    chat = client.models.generate_content(model="gemini-2.0-flash-001", contents=messages)
    print(chat.text)

    if verbose_checker():
        print(f"User prompt: {user_prompt}") 
        print(f"Prompt tokens: {chat.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {chat.usage_metadata.candidates_token_count}")

main()