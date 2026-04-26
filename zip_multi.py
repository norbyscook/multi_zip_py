from pathlib import Path
import subprocess
import os

# zips all directory and files in the root directory path into their respective folders 
# and move them to a new location: zip file destination

def main():
    print("enter root directory path: ")
    root_path = Path(input())

    print("enter zip file destination: ")
    zip_root = Path(input())
    # sub directory is the directory we will zip
    for sub_directory in root_path.iterdir():

        sub_directory_name = sub_directory.name
        sub_dir_zip_name = sub_directory_name + ".7z"
        zipto_location = zip_root.joinpath(sub_dir_zip_name)

        # if sub directory is a folder
        if sub_directory.is_dir():
            # optional: if folder is empty, don't zip
            directory_size = len(os.listdir(sub_directory))
            if(directory_size > 0):
                zip_tool = Zipper(zipto_location)     
                # zip items in sub directory in such a way that the zip file does not contain an extra layer of folder
                for deep_directory in sub_directory.iterdir():
                    zip_tool.append_argument(deep_directory)
                zip_tool.zip_file()
        else:
            # zip single files directly into it's own folder
            zip_tool = Zipper(zipto_location) 
            zip_tool.append_argument(sub_directory)
            zip_tool.zip_file()

class Zipper:
    def __init__(self, zip_dir):
        self.process_arg = ["7z", "a", zip_dir]

    def zip_file(self):
        subprocess.call(self.process_arg)
    
    def append_argument(self, input_arg):
        self.process_arg.append(input_arg)

    def get_argument(self):
        return self.process_arg

if __name__ == "__main__":
    main() 