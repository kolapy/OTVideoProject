import os
import platform

def cleanup(project_folder):
    os.chdir(project_folder)
    for root, dirs, files in os.walk(project_folder, topdown=False):
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            if not os.listdir(dir_path):
                os.rmdir(dir_path)
                print(f"Deleted empty directory: {dir_path}")


if __name__ == "__main__":
    project_folder = os.path.dirname(os.path.realpath(__file__))
    cleanup(project_folder)
    input("Press Enter to exit...")
