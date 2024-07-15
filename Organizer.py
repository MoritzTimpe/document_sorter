from os import path
from os import listdir
from pathlib import Path
from os.path import isfile, join
import shutil


class Organizer:

    def __init__(self, Xpath):
        self.folderpath = Xpath
        self.ext = ''
        self.filepath_ext = ''
        self.filepath_file = ''
        self.files = [f for f in listdir(self.folderpath) if isfile(join(self.folderpath, f))]
        self.output = ['__init__ successful!']

    def get_file_type(self, file):
        try:
            self.ext = file.split(".")[-1].upper()
            self.output.append("Split filetype!")
        except:
            self.output.append("Couldn't split filetype!")

    def create_file_paths(self, file):
        self.filepath_ext = join(self.folderpath, self.ext)
        self.filepath_file = join(self.folderpath, file)
        self.output.append("Created filepaths!")

    def get_existance_of_folder(self):
        if path.exists(self.filepath_ext):
            self.output.append("Folder existance: True!")
            return True
        else:
            self.output.append("Folder existance: False!")
            return False

    def move_file(self, file):
        if self.get_existance_of_folder():
            shutil.move(self.filepath_file, join(self.filepath_ext, file))
            self.output.append("File moved!")
        else:
            Path(self.filepath_ext).mkdir(parents=True, exist_ok=True)
            self.output.append("Directory created!")
            shutil.move(self.filepath_file, join(self.filepath_ext, file))
            self.output.append("File moved!")

    def get_files(self):
        return self.files

    def get_log(self):
        return self.output