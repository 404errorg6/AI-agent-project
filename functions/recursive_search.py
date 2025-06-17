import os

def recursive_search(directory=None, working_directory=None):
    structure = {}
    path = working_directory
    if directory:
        path = os.path.join(working_directory, directory)
    if not os.path.exists(path):
        print(f'"{directory}" doesn\'t exist, exiting...')
        exit()
    for dir_file in os.listdir(path):
        abs_path = os.path.join(path, dir_file)
        basename = os.path.basename(abs_path)
        if os.path.isfile(abs_path):
            structure[dir_file] = "file"
        elif os.path.isdir(abs_path) and basename[0].isalpha() and basename != "venv":
            structure[dir_file] = recursive_search(working_directory=abs_path)
    return structure
