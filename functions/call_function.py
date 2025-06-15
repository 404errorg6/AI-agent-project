from functions.get_file_content import get_file_content
from functions.get_files_info import get_files_info
from functions.run_python import run_python_file
from functions.write_file import write_file
from google.genai import types



def call_function(function_call_part, verbose=False):
    funcs = {
        "run_python_file" : run_python_file,
        "get_file_content" : get_file_content,
        "get_files_info" : get_files_info,
        "write_file" : write_file
    }
    function_name = function_call_part.name
    if verbose:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_name}")

    function_result = funcs[function_name]("./calculator", **function_call_part.args)
    if function_name not in funcs:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"error": f"Unknown function: {function_name}"},
                )
            ],
        )
    else:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"result": function_result},
                )
            ],
        )