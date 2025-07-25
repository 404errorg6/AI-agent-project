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
from functions.delete_file import delete_file
from functions.recursive_search import recursive_search
from functions.find_files import find_files
from functions.mkdir_rmdir import create_dir, del_dir
from functions.main_get_dir import get_dir
from functions.main_verbose_checker import verbose_checker

working_directory = get_dir()

def main():
            
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    
    
    client = genai.Client(api_key=api_key)
    
    try:
        user_prompt = sys.argv[1]
    except:
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here" [--verbose] [-d] <directory_path>')

        print('Example: python main.py "How do I fix the calculator?"')
        sys.exit(1)
        
    messages = [
        types.Content(role="user", parts=[types.Part(text=system_prompt + '\n' + user_prompt)])
    ]

    create_dir(".tmp", os.getcwd())
    try:
        generate_content(client, messages, verbose_checker())
    except Exception as e: #Exit with error handling
        print(f'Error: {e}')
        print("Exiting...")
        final_check = input('Do you want to delete the ".tmp" directory?(y/n): ')
        if final_check.lower() == "y":
            del_dir(".tmp", os.getcwd())
        sys.exit()
        
def generate_content(client, messages, verbose):
    i = 0
    while i < 20:
        response = client.models.generate_content(
            model="gemini-2.0-flash-001",
            contents=messages,
            config=types.GenerateContentConfig(
                tools=[available_functions], system_instruction=None
            ),
        )
        function_called = bool(response.function_calls)
        for candidate in response.candidates:
            messages.append(candidate.content)
        if not function_called:
            print(response.text)
            loop_check = input('Enter prompt to continue or "exit" to exit: ')
            if loop_check == "exit":
                final_check = input('Do you want to delete the ".tmp" directory?(y/n): ')
                if final_check.lower() == "y":
                    del_dir(".tmp", os.getcwd())
                sys.exit()
            else:
                messages.append(types.Content(role="user", parts=[types.Part(text=loop_check)]))
                i = 0
                continue
            
        else:
            tool_responses = []
            for function_call_part in response.function_calls:
                function_call_result = call_function(function_call_part=function_call_part, working_directory=working_directory, verbose=verbose)
                if (not function_call_result.parts or not function_call_result.parts[0].function_response):
                    raise Exception("Result of empty function call")
                tool_responses.append(
                    types.Content(role="tools", parts=[function_call_result.parts[0]])
                )
                if verbose:
                    print(f"->{function_call_result.parts[0].function_response.response}")
            messages.extend(tool_responses)
            i += 1
            continue

        if verbose:
            print("Prompt tokens:", response.usage_metadata.prompt_token_count)
            print("Response tokens:", response.usage_metadata.candidates_token_count)



if __name__ == "__main__":
    main()