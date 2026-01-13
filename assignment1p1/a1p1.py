
from pathlib import Path


def print_values(list_name):
    for item in list_name:
        print(item)


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


def list_only_files(path):
    p = Path(path)
    all_files = []

    for item in p.iterdir():
        if item.is_file():
            all_files.append(item)

    print_values(all_files)


def list_only_files_recursively(path):
    p = Path(path)
    all_files = []

    for item in p.rglob("*"):
        if item.is_file():
            all_files.append(item)

    print_values(all_files)


def list_exact_filename(path, file_name):
    p = Path(path)
    all_files = []

    for item in p.iterdir():
        if item.is_file() and item.name == file_name:
            all_files.append(item)

    print_values(all_files)


def list_exact_filename_recursively(path, file_name):
    p = Path(path)
    all_files = []

    for item in p.rglob("*"):
        if item.is_file() and item.name == file_name:
            all_files.append(item)

    print_values(all_files)


def list_files_extensions(path, extension_name):
    p = Path(path)
    all_files = []

    for item in p.iterdir():
        if item.is_file() and item.suffix[1:] == extension_name:
            all_files.append(item)

    print_values(all_files)


def list_files_extensions_recursively(path, extension_name):
    p = Path(path)
    all_files = []

    for item in p.rglob("*"):
        if item.is_file() and item.suffix[1:] == extension_name:
            all_files.append(item)

    print_values(all_files)


def main():
    # command, path = input().split(" ")
    print("list (not recursively)")
    list_files("testdir")
    print("\nlist recursively")
    list_recursively("testdir")
    print("\nlist only files")
    list_only_files("testdir")
    print("\nlist only files recursively")
    list_only_files_recursively("testdir")
    print("\nlist only files with specific name")
    list_exact_filename("testdir", "testfile1.txt")
    print("\nlist only files with specific name recursively")
    list_exact_filename_recursively("testdir", "testfile1.txt")
    print("\nlist only files with specific extension")
    list_files_extensions("testdir", "txt")
    print("\nlist only files with specific extension recursively")
    list_files_extensions_recursively("testdir", "py")


if __name__ == "__main__":
    main()
