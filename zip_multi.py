from pathlib import Path
import subprocess
import os

def main():
    print("enter root directory path: ")
    root_path = Path(input())

    print("enter zip file destination: ")
    zip_root = Path(input())

    for sub_directory in root_path.iterdir():
        sub_directory_name = sub_directory.name
        
        zip_location = zip_root.joinpath(sub_directory_name)
        if sub_directory.is_dir():
            dir_size = len(os.listdir(sub_directory))
            if(dir_size > 0):
                zip_tool = Zipper(zip_location)     
                for deep_directory in sub_directory.iterdir():
                    # print(deep_directory)
                    zip_tool.append_argument(deep_directory)
                # print(zip_tool.get_argument())
        else:
            zip_tool = Zipper(zip_location) 
            zip_tool.append_argument(sub_directory)
            # print(zip_tool.get_argument())
            

class Zipper:
    def __init__(self, zip_dir):
        self.process_arg = ["7z", "a", zip_dir]

    def zip_file(self, zip_location):
        subprocess.call(self.process_arg)
    
    def append_argument(self, input_arg):
        self.process_arg.append(input_arg)

    def get_argument(self):
        return self.process_arg


if __name__ == "__main__":
    main() 