"""

Inspired by (and likely ripping off) https://github.com/eric-mahasi/downloads-folder-automation/blob/main/downloads_folder_sorter.py
Seems useful considering how ungodly my downloads folder has become.

This file contains the following functions:
    * move_file   -> checks to see if the destination dir exists, otherwise creates it and then moves the file into it
    * sort_folder -> iterates through the files in the folder using the move_file function

"""

import os
import shutil
from pathlib import Path
import json
import datetime

with open('config.js', encoding='utf-8') as f:
    CATEGORIES = json.load(f)

def move_file(file, destination):
    try:
        if not destination.exists():
            destination.mkdir(parents=True, exist_ok=True)
        if os.path.exists(str(destination) + str(file)):
            os.rename(str(file), str(file) + '-' + datetime.datetime.now().strfmt(format='%d%m%Y'))
        shutil.move(str(file), str(destination))

    except shutil.Error as e:
        print(e)

def sort_folder(folder_path):
    for file in folder_path.iterdir():
        if file.is_file():
            for category in CATEGORIES:
                if file.suffix in category['extensions']:
                    destination = file.parent.joinpath(category['name'])
                    move_file(file, destination)

if __name__ == '__main__':
    user = os.getlogin()
    paths = ['downloads','desktop']
    for path in paths:
        downloads_path = Path("/Users/{}/{}".format(user, path))
        print(downloads_path)
        sort_folder(downloads_path)
