import os
import sys
from datetime import datetime


def create_directory(directory_path: str) -> None:
    os.makedirs(directory_path)
    print(f"{directory_path} directory created.")


def create_file(file_path: str) -> None:
    with open(file_path, "a") as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"\n{timestamp}\n")

        print(f"(to stop the program write 'stop')")
        line_counter = 1
        while True:
            line = input("Enter content line: ")
            if line.lower() == "stop":
                break
            f.write(f"{line_counter} {line}\n")
            line_counter += 1

    print(f"File {file_path} created successfully.")


def main() -> None:
    directory_path = ""
    args = sys.argv[1:]
    if not args:
        raise ValueError("No arguments provided. Use '-d' to create "
                         "directories or '-f' to create a file.")

    if "-d" in args:
        dir_index = args.index("-d") + 1
        directory_parts = []
        while dir_index < len(args):
            directory_parts.append(args[dir_index])
            dir_index += 1
        directory_path = os.path.join(*directory_parts)
        create_directory(directory_path)

    if "-f" in args:
        file_index = args.index("-f") + 1
        if file_index < len(args):
            file_name = args[file_index]
            file_path = os.path.join(directory_path, file_name)
            create_file(file_path)
        else:
            raise ValueError("Please write a file name after '-f'.")

    if not directory_path and "-f" not in args:
        raise ValueError("Neither '-d' nor '-f' flag provided.")


if __name__ == "__main__":
    try:
        main()
    except ValueError as e:
        print(f"Error: {e}")
