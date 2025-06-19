import os

def delete_file(file_path, working_directory=None):
    if not working_directory:
        working_directory = os.getcwd()
    abs_path = os.path.join(working_directory, file_path)
    basename = os.path.basename(abs_path)
    try:
        os.remove(abs_path)
        print(f'File "{basename}" deleted successfully.')
    except FileNotFoundError:
        print(f'Error: File "{basename}" not found.')
    except Exception as e:
        print(f'Error deleting file "{basename}": {e}')
