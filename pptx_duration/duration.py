from tinytag import TinyTag
import glob
import datetime
from zipfile import ZipFile
import shutil
import os
import sys

def main():
    path = sys.argv[1]
    folder, _ = os.path.split(path)
    temp_folder = folder + "\\temp"

    with ZipFile(path, 'r') as zObject:
        zObject.extractall(temp_folder)

    file_list = glob.glob(temp_folder + "\\ppt\\media\\" + "*.m4a")

    total_time = 0
    for filename in file_list:
        tag = TinyTag.get(filename)
        total_time += tag.duration

    print(f"Total Time = {datetime.timedelta(seconds=total_time)}")

    shutil.rmtree(temp_folder)



if __name__ == "__main__":
    main()