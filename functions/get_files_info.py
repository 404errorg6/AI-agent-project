import os

def get_files_info(working_directory, directory=None):
    working_directory = os.path.abspath(working_directory)
    if directory:
        cmp_dir = os.path.abspath(os.path.join(working_directory, directory))
    if directory in [".", None]:
        cmp_dir = working_directory
    try:
        if cmp_dir.startswith(working_directory):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(cmp_dir):
            return f'Error: "{directory}" is not a directory'
        
        
        else:
            splitted = []
            contents = os.listdir(cmp_dir)
            for content in contents:
                cmp_path = os.path.join(cmp_dir, content)
                is_dir = os.path.isdir(cmp_path)
                file_size = os.path.getsize(cmp_path)
                final = f"- {content}: file_size={file_size} bytes, is_dir={is_dir}"
                splitted.append(final)
            joined = "\n".join(splitted)
            return joined
    except Exception as e:
        return f"Error: {e}"