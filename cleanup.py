import os
import time
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def cleanup(project_folder):
    print(f"Working in directory: {project_folder}")

    # Collect all directories before the deletion process starts
    all_directories = []
    for root, dirs, files in os.walk(project_folder, topdown=False):
        all_directories.extend(dirs)

    print(f"Directories before deletion: {all_directories}")

    # Start the deletion process
    for dir_name in all_directories:
        dir_path = os.path.join(project_folder, dir_name)
        try:
            if not os.listdir(dir_path):
                os.rmdir(dir_path)
                print(f"{Fore.GREEN}Deleted empty directory:{Style.RESET_ALL} {dir_path}")
        except Exception as e:
            print(f"{Fore.RED}Error deleting directory:{Style.RESET_ALL} {dir_path}")

if __name__ == "__main__":
    project_folder = os.getcwd()
    print(f"Project folder: {project_folder}")


    try:
        print("Initializing...")
        time.sleep(5)
        cleanup(project_folder)
    except Exception as e:
        print(f"{Fore.RED}Exception during cleanup:{Style.RESET_ALL}")

    input("Press Enter to exit...")



