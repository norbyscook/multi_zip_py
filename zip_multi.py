import os
import subprocess

print("enter root directory path: ")
root_directory_path = input()

print("enter zip file destination: ")
zip_destination = input()

os.chdir(root_directory_path)
subprocess.check_call(["powershell", "dir"])
sub_directories = os.listdir(root_directory_path)

for directory in sub_directories:
    directory_name = '"' + directory + '"'
    zip_name = '"' + zip_destination + "\\" + directory + '.7z"'
    subprocess.call(["7z", "a", zip_name, directory_name])


#     subprocess.call("7z " + "a " + zip_name + " " + directory_name)
