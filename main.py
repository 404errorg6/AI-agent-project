import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from config import system_prompt, available_functions
from functions.call_function import call_function
from functions.get_file_content import get_file_content
from functions.get_files_info import get_files_info
from functions.run_python import run_python_file
from functions.write_file import write_file

def verbose_checker():
    try:
          return "--verbose" in sys.argv
    except IndexError:
         return 0

def generate_content(client, messages, verbose):
    
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions], system_instruction=system_prompt
        ),
    )
    
    if not response.function_calls:
        print(response.text)
    else:
        for function_call_part in response.function_calls:
            function_call_result = call_function(function_call_part=function_call_part, verbose=verbose)
        
            if function_call_result.parts[0].function_response.response and verbose:
                print(f"-> {function_call_result.parts[0].function_response.response}")
            else:
                raise Exception("Fatal error: Unable to produce response")

    if verbose:
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)



def main():
        
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    
    
    client = genai.Client(api_key=api_key)
    
    try:
        user_prompt = sys.argv[1]
    except:
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here" [--verbose]')
        print('Example: python main.py "How do I fix the calculator?"')
        sys.exit(1)
        
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)])
    ]


    generate_content(client, messages, verbose_checker())





if __name__ == "__main__":
    main()

