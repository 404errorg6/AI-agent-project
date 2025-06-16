import os
import shutil

def create_temp_dir(path=None):
    abs_path = None
    if path:
        abs_path = os.path.abspath(path)
        check = 1
    elif path in [None, "."]:
        abs_path = os.getcwd()
        check = 0
    os.makedirs(abs_path + "/tmp", exist_ok=True)
    print(f'Successfully created "tmp" directory in path: {abs_path}')

def del_temp(path=None):
    if path:
        abs_path = os.path.abspath(path)
        check = 1
    elif path in [None, "."]:
        abs_path = os.getcwd()
        check = 0
    shutil.rmtree(abs_path + "/tmp")
    print(f'Successfully removed "tmp" directory in path: {path if check else os.path.basename(abs_path)}')
