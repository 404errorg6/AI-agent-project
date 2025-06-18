import os
from functions.get_file_content import get_file_content
from functions.get_files_info import get_files_info
from functions.run_python import run_python_file
from functions.write_file import write_file
from functions.delete_file import delete_file
from functions.recursive_search import recursive_search
from functions.find_files import find_files
from functions.mkdir_rmdir import create_dir, del_dir
from google.genai import types



def call_function(function_call_part, verbose=False):
    funcs = {
        "run_python_file" : run_python_file,
        "get_file_content" : get_file_content,
        "get_files_info" : get_files_info,
        "write_file" : write_file,
        "delete_file" : delete_file,
        "recursive_search" : recursive_search,
        "find_files" : find_files,
        "del_dir" : del_dir,
        "create_dir" : create_dir
    }
    function_name = function_call_part.name
    if verbose:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_name}")

    try:
        # Remove working_directory from args to avoid duplicate argument error
        args = function_call_part.args.copy()
        args.pop('working_directory', None)
        function_result = funcs[function_name](working_directory=os.getcwd(), **args)
        return types.Content(
            role="model",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"result": function_result},
                )
            ],
        )
    except Exception as e:
        return types.Content(
            role="model",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"error": f"Function {function_name} failed: {str(e)}"},
                )
            ],
        )

