import subprocess

project_path = "./path/to/"
try:
    subprocess.check_call(["pipreqs", project_path])
    print("requirements.txt has been successfully generated.")
except subprocess.CalledProcessError as e:
    print("An error occurred while generating requirements.txt: ", e)
