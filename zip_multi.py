from pathlib import Path
import subprocess

print("enter root directory path: ")
root_path = "H:\Not Backed Up\\test zip\Hello"

print("enter zip file destination: ")
zip_destination = "H:\Not Backed Up\\test zip\zipped hello"

for sub_directory in root_path.iterdir():
    if subdir.is_dir():
        print(sub_directory)