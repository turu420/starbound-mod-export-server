import shutil
import glob
import os


import os

def get_files(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield file


dirs = [ f.path for f in os.scandir("./") if f.is_dir() ]



for i in dirs:
    if i == './export':
        dirs.remove(i)


for i in dirs:
    files = get_files(i)

    for file in files:
        print(file)

    pathOld = i + "/" + file

    pathNew = './export/' + i[2:] + ".pak"


    print(f"Old Path: {pathOld}, New Path: {pathNew}")
    shutil.copyfile(pathOld, pathNew)
    print("COPIED")



print("DONE!!!")
print("Have a great time with your server c:")