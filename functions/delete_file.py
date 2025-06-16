import os

def delete_function(working_directory, target_path):
    abs_wd = os.path.abspath(working_directory)
    abs_target_path = os.path.abspath(target_path)
    if os.path.isdir(abs_target_path):
        #os.getcwd()
        