import os
from pathlib import Path

SUBDIRECTORIES = {
    "DOCUMENTS": ['.pdf','.rtf','.txt'],
    "AUDIO": ['.m4a','.m4b','.mp3'],
    "VIDEOS": ['.mov','.avi','.mp4'],
    "IMAGES": ['.jpg','.jpeg','.png']
}

def pickDirectory(value):
    for category, suffixes in SUBDIRECTORIES.items():
        for suffix in suffixes:
            if suffix == value:
                return category
    return 'MISC'

def organizeDirectory():
    for item in os.scandir():
        if item.is_dir():
            continue
        filePath = Path(item) # get file path
        fileType = filePath.suffix.lower()
        directory = pickDirectory(fileType)
        directoryPath = Path(directory) # get dir relative path
        print(filePath, fileType, directory, directoryPath)
        if directoryPath.is_dir() != True:
            directoryPath.mkdir()
        filePath.rename(directoryPath.joinpath(filePath)) # mv file dir/file

organizeDirectory()

# os.scandir() scans only the first layer of direcotry, 
# so if you want to traverse all the file in a directory, recursive is required

# def print_files_in_directory(directory):
#     for entry in os.scandir(directory):
#         if entry.is_file():
#             print(entry.path)
#         elif entry.is_dir():
#             print_files_in_directory(entry.path)

# print_files_in_directory('OrganizeMe')

