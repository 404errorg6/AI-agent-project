import os 


def get_file_content(working_directory, file_path):
    
    try:
        working_directory = os.path.abspath(working_directory)
        cmp_fpath = os.path.abspath(os.path.join(working_directory, file_path))
        if not cmp_fpath.startswith(working_directory):
            return f'Error: Cannot read "{file_path}" as it is outside permitted working directory'
        if not os.path.isfile(cmp_fpath):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        else:
            MAX_CHARS = 10000
            with open(cmp_fpath, "r") as f:
                file_content_string = f.read(MAX_CHARS)
                if len(file_content_string) == MAX_CHARS:
                    file_content_string += f'\n[...File "{file_path}" truncated at {MAX_CHARS} characters]'
                return file_content_string
            
    except Exception as e:
        return f'Error reading file "{file_path}": {e}'
