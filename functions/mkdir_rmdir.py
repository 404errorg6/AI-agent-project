import os
import shutil

def create_dir(path, working_directory=None):
    basename = os.path.basename(path)
    if path in [None, "."]:
        raise Exception('Directory name not given')
    abs_path = os.path.join(working_directory, path)
    os.makedirs(abs_path, exist_ok=True)
    return f'Successfully created "{basename}" directory in path: {abs_path}'


def del_dir(path, working_directory=None):
    basename = os.path.basename(path)
    try:
        if path in [None, "."]:    
            raise Exception('Directory name not given')
        abs_path = os.path.join(working_directory, path)
        shutil.rmtree(abs_path)
        return f'Successfully removed "{basename}" directory in path: {abs_path}'

    except FileNotFoundError:
        print(f'"{basename}"  directory not found')

    except NotADirectoryError:
        print(f'"{basename}" is a file not a directory')
    
    except Exception as e:
        print(f'Error while deleting "{basename}": {e}')

