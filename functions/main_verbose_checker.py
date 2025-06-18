import sys

def verbose_checker():
    try:
          return "--verbose" in sys.argv
    except IndexError:
         return 0