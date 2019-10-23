import os
import sys
import shutil

basepath = sys.argv[1]

if not str(basepath).endswith("/"):
    basepath += "/"

ffMapping = [["docx", "Documents-Word Documents"],
             ["pdf", "Documents-PDFs"],
             ["dmg", "System Files-Disk Images"],
             ["zip", "Documents-Compressed Files"],
             ["txt", "Documents-Text Documents"]]

def delete(file):
    shutil.rmtree(file)
    print("Removed " + file)


def handleAppFile(file):
    if os.path.exists(os.path.join(file)):
        delete(file)
    else:
        print(os.path.join(file) + " doesn't exist, you may want to install it")

def moveFile(file):
    for extension in ffMapping:
        if str(file).endswith(extension[0]):
            pathToMoveTo = basepath
            tree = extension[1].split("-")
            if tree[0] == "Documents" or tree[0] == "Desktop":
                pathToMoveTo = os.path.expanduser("~/" + tree[0] + "/")
            else:
                if not os.path.exists(pathToMoveTo + tree[0]):
                    os.mkdir(os.path.join(pathToMoveTo + tree[0]))
                pathToMoveTo += tree[0] + "/"
            tree.remove(tree[0])
            for subfolder in tree:
                if not os.path.exists(pathToMoveTo + subfolder):
                    os.mkdir(os.path.join(pathToMoveTo + tree[0]))
                pathToMoveTo += subfolder + "/"
            pathToMoveTo += file
            print("Moving " + file + " to " + pathToMoveTo)
            shutil.move(basepath + file, pathToMoveTo)


for filename in os.listdir(basepath):
    filepath = basepath + filename
    if filename.endswith(".app"):
        handleAppFile(filepath)
    else:
        moveFile(filename)
