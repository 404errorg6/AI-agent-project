import os
import sys

def delete_file(file_path, working_directory=None):
    try:
        os.remove(file_path)
        print(f'File "{file_path}" deleted successfully.')
    except FileNotFoundError:
        print(f'Error: File "{file_path}" not found.')
    except Exception as e:
        print(f'Error deleting file "{file_path}": {e}')

if __name__ == "__main__":
    if len(sys.argv) > 1:
        file_to_delete = sys.argv[1]
        delete_file(file_to_delete)
    else:
        print("Missing one required argument")
        print("Usage: python3 delete_file.py <file>")

#delete_file("lol.py")