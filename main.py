from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table
import shutil
import re
import os

def make_directory(directory):
    if os.path.exists(directory):
        return
    os.mkdir(directory)

def move_user2(directory):
    make_directory(directory)
    shutil.move("./user-docs/user2", directory)

def sort_directory(directory):
    extension = '.log'

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                make_directory(os.path.join(directory,"logs"))
                shutil.move(os.path.join(root, file), os.path.join(directory, "logs"))
            elif file.endswith(".mail"):
                make_directory(os.path.join(directory,"mail"))
                shutil.move(os.path.join(root, file), os.path.join(directory, "mail"))


def parse_error_directory(directory):
    for root, dirs, files, in os.walk(directory):
        for file in files:
            if file.endswith(".log"):
                errors = []
                warnings = []

                with open(os.path.join(root, file), 'r') as reading:
                    line = reading.readline()
                    match = re.search(r'ERROR', line)
                    if match:
                        errors.append(line)
                    match = re.search(r'WARNING', line)
                    if match:
                        warnings.append(line)
                
                with open(os.path.join(root,"errors.log"), 'w') as file:
                    for element in errors:
                        file.write(element + "\n")
                with open(os.path.join(root,"warnings.log"), 'w') as file:
                    for element in warnings:
                        file.write(element + "\n")


def main():
    while True:

        console.print("\n1. Make a new folder\n2. Handle deleted user2\n3. Sort documents\n4. Parse log\n5. Exit")
        choice = Prompt.ask("Choose a task", choices=['1', '2', '3', '4', '5'], default='5')

        if choice == '1':
            directory = Prompt.ask("Enter the new folder to be created")
            make_directory(directory)
        elif choice == '2':
            directory = Prompt.ask("Enter the name of the temporary folder")
            move_user2(directory)
        elif choice == '3':
            directory = Prompt.ask("Enter the name of the directory to be sorted")
            sort_directory(directory)
        elif choice == '4':
            directory = Prompt.ask("Enter the target directory for logs")
            parse_error_directory(directory)
        else:
            break

if __name__ == "__main__":
    console = Console()
    main()