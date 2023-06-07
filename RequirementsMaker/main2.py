import os
import subprocess

root_path = "./"  # Change this to your project root path

# Loop over all directories in the root_path
for dirpath, dirnames, filenames in os.walk(root_path):
    if dirnames:  # Ignore leaf directories
        for dirname in dirnames:
            full_dir_path = os.path.join(dirpath, dirname)
            try:
                subprocess.check_call(["pipreqs", full_dir_path])
                print(f"requirements.txt has been successfully generated in {full_dir_path}")
            except subprocess.CalledProcessError as e:
                print(f"An error occurred while generating requirements.txt in {full_dir_path}: ", e)

