import os
import re

def find_files(directory=None, pattern=".*", working_directory="."):
    """
    Searches for files matching a specific pattern within a directory and its subdirectories.

    Args:
        directory: The directory to start searching from. If None, defaults to the working_directory.
        pattern: The regular expression pattern to match filenames against (default: match all files).
        working_directory: The directory to use if directory is None. Defaults to ".".

    Returns:
        A list of absolute paths to files that match the pattern.
    """
    if directory is None:
        directory = working_directory
    matches = []
    for root, _, filenames in os.walk(directory):
        for filename in filenames:
            if re.match(pattern, filename):
                try:
                    matches.append(os.path.join(root, filename))
                except Exception as e:
                    print(f"Error joining path: {e}")
    return matches

if __name__ == '__main__':
    # Example usage:
    # Find all python files in the current directory and its subdirectories
    python_files = find_files(pattern=r".*\.py$")
    if python_files:
        print(f"Found python files: {python_files}")
    else:
        print("No python files found.")

    # Find all files starting with 'test' in the current directory and its subdirectories
    test_files = find_files(directory=".", pattern=r"^test.*")
    if test_files:
        print(f"Found test files: {test_files}")
    else:
        print("No test files found starting with 'test'.")

    # Find files in a specific working directory
    files_in_tmp = find_files(pattern=".*", working_directory=".tmp")
    if files_in_tmp:
        print(f"Files in .tmp: {files_in_tmp}")
    else:
        print("No files found in .tmp")