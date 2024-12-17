import sys
import os

METHOD_LIST = ["copy", "duplicate-contents", "reverse", "replace-string"]

def new_file_with_reversed_contents(input_path: str, output_path: str) -> None:
    contents = ''
    with open(input_path) as f:
        contents = f.read()

    reversed_contents = contents[::-1]

    with open(output_path, 'w') as f:
        f.write(reversed_contents)

def copy_file(input_path: str, output_path: str) -> None:
    with open(input_path) as f:
        contents = f.read()

    with open(output_path, 'w') as f:
        f.write(contents)

def duplicate_contents(input_path: str, count: int) -> None:
    contents = ''
    with open(input_path) as f:
        contents = f.read()

    duplicated_contents = contents * count

    with open(input_path, 'w') as f:
        f.write(duplicated_contents)

def replace_string(input_path: str, needle: str, new_string: str) -> None:
    contents = ''
    with open(input_path) as f:
        contents = f.read()

    replaced_contents = contents.replace(needle, new_string)

    with open(input_path, 'w') as f:
        f.write(replaced_contents)

args = sys.argv
if len(args) < 4:
    print("Usage: python file_manipulator.py <method> <input_path> <output_path>")
    exit()

method = args[1]
input_path = args[2]

if method not in METHOD_LIST:
    print(f"Invalid method: {method}")
    exit()

if not os.path.exists(input_path):
    print(f"File not found: {input_path}")
    exit()

match method:
    case "copy":
        copy_file(input_path, args[3])
    case "duplicate-contents":
        try:
            duplicate_contents(input_path, int(args[3]))
        except ValueError:
            print("Invalid count")
            exit()
    case "reverse":
        new_file_with_reversed_contents(input_path, args[3])
    case "replace-string":
        replace_string(input_path, args[3], args[4])
    case _:
        print(f"Invalid method: {method}")
        exit()

print("Done")
