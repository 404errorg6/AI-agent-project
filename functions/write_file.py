import os

def write_file(working_directory, file_path, content):
    working_directory = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not abs_file_path.startswith(working_directory):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    if os.path.exists(abs_file_path) and os.path.isdir(abs_file_path):
        return f'Error: {file_path} is a directory not a file'
    try:
    
        os.makedirs("/".join(abs_file_path.split("/")[0:-1]), exist_ok=True)
        with open(abs_file_path, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f'Error while writing to "{file_path}": {e}'