import os
import sys

def get_dir():
    try:
        if "-d" in sys.argv:
            index = sys.argv.index("-d") + 1
            directory = sys.argv[index]
            abs_dir = os.path.join(os.getcwd(), directory)
            if not os.path.exists(abs_dir):
                raise FileNotFoundError(f'Error: "{directory}" directory not found')
            return abs_dir
        else:
            return os.getcwd()
    except IndexError:
        raise IndexError(f'No directory path provided after "-d" flag')
    except FileNotFoundError as e:
        raise FileNotFoundError(f'{e}')