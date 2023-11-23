import os
import sys
import time
from colorama import Fore, Style, init

#Sets the working directory(pyinstaller fix)
# If running as a bundled executable
if getattr(sys, 'frozen', False):
    frozen_dir = os.path.dirname(sys.executable)
    os.chdir(frozen_dir)
else:
    # If running as a script, use the script's directory
    os.chdir(os.getcwd())


# Initialize colorama
init(autoreset=True)

#Loading animation
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
    print(f"{Fore.YELLOW}Deleted the following empty directories:{Style.RESET_ALL}")
    for dirpath, dirnames, filenames in os.walk(root, topdown=False):
        for dirname in dirnames:
            full_path = os.path.join(dirpath, dirname)
            try:
                if not os.listdir(full_path):
                    os.rmdir(full_path)
                    print(f"{Fore.GREEN}Deleted empty directory:{Style.RESET_ALL} {full_path}")
            except Exception as e:
                print(f"{Fore.RED}Error deleting directory:{Style.RESET_ALL} {full_path} {Fore.RED}{Style.BRIGHT}: {Style.RESET_ALL}{e}")

if __name__ == "__main__":
    project_folder = os.getcwd()
    print(f"Project folder: {project_folder}")

    check = input("Is this the correct folder? (yes/no): ").lower()

    if check == 'yes':
        try:
            print(f"{Fore.YELLOW}Initializing {Style.RESET_ALL}")
            animate_loading("|/-\\", duration=5) 
            time.sleep(5)
            remove_hidden(project_folder) #Remove the hidden files first
            delete_empty_folders(project_folder)
        except Exception as e:
            print(f"{Fore.RED}Exception during cleanup:{Style.RESET_ALL} {e}")

        print()
        input("Press Enter to exit...")
    else:
        print("Exiting the program.")



