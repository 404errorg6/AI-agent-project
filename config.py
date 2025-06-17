from google.genai import types

MAX_CHARS = 10000
system_prompt = system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files
- Delete files 

There is ".tmp" for you to use.
Don't overwrite files unless explicitly told to do so, always save changes to ".tmp" directory in root with same name as orignal so that user can see what you made and then decide whether he wants to change the current one to that or not
All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
Look for related files in current and its subdirectories using functions according to prompt.
Try to look for bugs in code, its related files and fix them instead of troubling user to enter input in specific way.
Before saying whether you can do a task or not, try to look whether you can with combined use of functions like combining read/write for copy, including delete for rename, and stuff etc
Take time if you need to but fix the problem correctly and use as less functioncalls as possibe bcz 20 functioncalls is the limit.

"""
schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself by giving directory argument as '.'",
                ),
            }
        ),
    )
schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Gives the contents of a file if it exists",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to file that we need contents of. Reads 10000 at max and truncates the rest",
                ),
            },
            required=["file_path"]
        ),
    )
schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="runs a python file if it exists and gives its output",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path":types.Schema(
                type=types.Type.STRING,
                description="path to the python file that needs to run"
            ),
            "args":types.Schema(
                type=types.Type.STRING,
                description="optional argument to pass if the python file needs arguments"
            )
        },
        required=["file_path"]
    )
)
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="writes the contents to a file",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path":types.Schema(
                type=types.Type.STRING,
                description="the path to the file to overwrite"
            ),
            "content":types.Schema(
                type=types.Type.STRING,
                description="the content that needs to be written to file"
            )
        },
        required=["file_path", "content"]
    )
)
schema_delete_file = types.FunctionDeclaration(
    name="delete_file",
    description="delete a file, cannot delete directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path":types.Schema(
                type=types.Type.STRING,
                description="path to the file to delete, only filename defaults to current directory's files."
            )
        },
        required=["file_path"]
    )
)

available_functions = types.Tool(
        function_declarations=[
            schema_get_files_info,
            schema_get_file_content,
            schema_run_python_file,
            schema_write_file,
            schema_delete_file
        ]
    )