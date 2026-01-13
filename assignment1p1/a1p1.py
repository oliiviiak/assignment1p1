
from pathlib import Path

def print_values(list_name):
    for item in list_name:
        print (item)

def list_files(path):
    p = Path(path)
    all_files = []
    all_dirs = []

    for item in p.iterdir():
        if item.is_file():
            all_files.append(item)
        else:
            all_dirs.append(item)
    
    print_values(all_files)
    print_values(all_dirs)

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
    print ("list (not recursively)")
    list_files("testdir")
    print ("\nlist recursively")
    list_recursively("testdir")


if __name__ == "__main__":
    main()