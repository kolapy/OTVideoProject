import os
import time
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def animate_loading(animation_sequence, duration=1):
    idx = 0
    start_time = time.time()

    while time.time() - start_time < duration:
        print(animation_sequence[idx % len(animation_sequence)], end="\r")
        idx += 1
        time.sleep(0.1)

        if idx == len(animation_sequence):
            idx = 0

    print(" " * len(animation_sequence), end="\r")  # Clear the animation

# Function to remove the gitkeep and DS store files before attempting to delete anything
def remove_hidden(project_folder):
    try:
        for root, dirs, files in os.walk(project_folder):
            for filename in ['.gitkeep', '.DS_Store']:
                file_path = os.path.join(root, filename)
                if os.path.exists(file_path):
                    os.remove(file_path)
                    print(f"{Fore.YELLOW}Removed file: {Style.RESET_ALL} {file_path}")
    except Exception as e:
        print(f"{Fore.RED}Error removing files globally: {Style.RESET_ALL} {e}")


def delete_empty_folders(root):
    dirList = []

    for dirpath, dirnames, filenames in os.walk(root, topdown=False):
        for dirname in dirnames:
            full_path = os.path.join(dirpath, dirname)
            try:
                if not os.listdir(full_path):
                    print(f"{Fore.YELLOW}Deleted the following empty directories:{Style.RESET_ALL}")
                    os.rmdir(full_path)
                    print(f"{Fore.GREEN}Deleted empty directory:{Style.RESET_ALL} {full_path}")
            except Exception as e:
                print(f"{Fore.RED}Error deleting directory:{Style.RESET_ALL} {full_path} {Fore.RED}{Style.BRIGHT}: {Style.RESET_ALL}{e}")
    

def cleanup(project_folder):
    print(f"Working in directory: {project_folder}")

    # Collect all directories before the deletion process starts
    all_directories = []
    for root, dirs, files in os.walk(project_folder, topdown=False):
        print(f"Current directory: {root}")
        print(f"Subdirectories: {dirs}")
        print(f"Files: {files}")
        print("--------------------")
        
        all_directories.extend(dirs)

    # Reverse the order of directories
    all_directories.reverse()

    print(f"Directories before deletion: {all_directories}")

    # Start the deletion process
    for dir_name in all_directories:
        dir_path = os.path.join(root, dir_name)
        try:
            print(f"{Fore.YELLOW}Attempting to delete: {Style.RESET_ALL}{dir_path}")
            if not os.listdir(dir_path):
                os.rmdir(dir_path)
                print(f"{Fore.GREEN}Deleted empty directory:{Style.RESET_ALL} {dir_path}")
        except Exception as e:
            print(f"{Fore.RED}Error deleting directory:{Style.RESET_ALL} {dir_path} {Fore.RED}{Style.BRIGHT}: {Style.RESET_ALL}{e}")

if __name__ == "__main__":
    project_folder = os.getcwd()
    print(f"Project folder: {project_folder}")


    try:
        print(f"{Fore.YELLOW} Initializing {Style.RESET_ALL}")
        animate_loading("|/-\\", duration=5) 
        time.sleep(5)
        remove_hidden(project_folder) #Remove the hidden files first
        delete_empty_folders(project_folder)
    except Exception as e:
        print(f"{Fore.RED}Exception during cleanup:{Style.RESET_ALL} {e}")

    input("Press Enter to exit...")



