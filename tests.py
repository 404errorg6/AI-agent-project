import os
from functions.run_python import run_python_file

def main():
    print(run_python_file(file_path="tmp/test_script.py"))

if __name__ == "__main__":
    main()