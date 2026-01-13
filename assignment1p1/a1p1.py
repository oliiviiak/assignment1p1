
from pathlib import Path

def print_values(list_name):
    for item in list_name:
        print (item)

def list_files(path):
    p = Path(path)
    all_files_dirs = []

    for item in p.iterdir():
        all_files_dirs.append(item)
    
    print_values(all_files_dirs)


def list_recursively(path):
    p = Path(path)
    all_files_dirs = []

    for item in p.rglob("*"):
        all_files_dirs.append(item)
    
    print_values(all_files_dirs)

"""def list_only_files(path):

def list_exact_files(path, file_name):

def list_files_extensions(path, extension_name):"""


def main():
    #command, path = input().split(" ")
    list_recursively("testdir")


if __name__ == "__main__":
    main()