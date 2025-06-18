import os

def delete_file(file_path, working_directory=None):
    try:
        os.remove(file_path)
        print(f'File "{file_path}" deleted successfully.')
    except FileNotFoundError:
        print(f'Error: File "{file_path}" not found.')
    except Exception as e:
        print(f'Error deleting file "{file_path}": {e}')
