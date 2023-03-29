from tinytag import TinyTag
import datetime
from pathlib import Path
from zipfile import ZipFile
import shutil
import sys

def main():
    if len(sys.argv) < 2:
        print("Please provide the path to a .pptx file.")
        sys.exit(1)

    file_path = Path(sys.argv[1])
    folder = file_path.parents[0]
    temp_folder = folder / "temp"

    with ZipFile(file_path, 'r') as zObject:
        zObject.extractall(temp_folder)

    media_folder = temp_folder / "ppt" / "media"
    file_list = media_folder.glob("*.m4a")

    total_time = 0
    for filename in file_list:
        tag = TinyTag.get(filename)
        total_time += tag.duration

    print(f"Total Time = {datetime.timedelta(seconds=total_time)}")

    shutil.rmtree(temp_folder)



if __name__ == "__main__":
    main()