import os
import shutil

def create_temp_dir(path=None):
    if path:
        abs_path = os.path.abspath(path)
    elif path in [None, "."]:
        abs_path = os.getcwd()
    os.makedirs(abs_path + "/.tmp", exist_ok=True)
    print(f'Successfully created "tmp" directory in path: {abs_path}')

def del_temp(path=None):
    try:
        if path:
            abs_path = os.path.abspath(path)
        elif path in [None, "."]:
            abs_path = os.getcwd()
        abs_path = os.path.join(abs_path, ".tmp")
        shutil.rmtree(abs_path)
        basename = os.path.basename(abs_path)
        print(f'Successfully removed "{basename}" directory in path: {abs_path}')

    except FileNotFoundError:
        print("No tmp directory found")

    except NotADirectoryError:
        print(f'"{basename}" is a file not a directory')
    
    except Exception as e:
        print(f"Error while deleting tmp: {e}")
