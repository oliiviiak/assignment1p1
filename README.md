
# Program Description
The file system inspector is a Python program that allows users to inspect
directory contents using various listing commands. The commands support
recursive searching, file-only listing, filtering by filename,
and filtering by file extensions.

# Command Format
[COMMAND] [INPUT] [[-]OPTION] [INPUT]

# All Commands
L - List the contents of the user specified directory.
Q - Quit the program.

Options of the 'L' command
    -r Output directory content recursively.
    -f Output only files, excluding directories in the results.
    -s Output only files that match a given file name.
    -e Output only files that match a given file extension.
