import os
import pathlib
import shutil

from pathlib import Path

gah = str(Path.home())

DOWNLOADS = gah + "/" + 'Downloads/'

path = DOWNLOADS
file_name = os.listdir(path)

#if you need more folders, simply add them in the 'folder_names' list below, using it as an example.
#removing folders is more tricky, as you'll need to change where those files would've went in the if/elif statements below.

folder_names = ['image files', 'text files', 'applications', 'document files', 'video files', 'audio files', 'misc files']

lengthFoldernames = len(folder_names)

for loop in range(0,lengthFoldernames):
    if not os.path.exists(path + folder_names[loop]):
        print(path + folder_names[loop])
        os.makedirs(path + folder_names[loop])

#if the file extensions you have do not apply to this list, simply copy paste one of the elif statements.
#then, in the first quotations, replace with the file extension you need to account for, i.e. ".exe".
#finally, make sure it goes into the correct folder by replacing the last two quotations with the correct category.
#i.e 'applications/' the '/' is important for it not to mess up.

for file in file_name:
    if ".url" in file and not os.path.exists(path + 'applications/' + file):
        shutil.move(path + file, path + 'applications/' + file)

    elif ".exe" in file and not os.path.exists(path + 'applications/' + file):
        shutil.move(path + file, path + 'applications/' + file)

    elif ".msi" in file and not os.path.exists(path + 'applications/' + file):
        shutil.move(path + file, path + 'applications/' + file)

    elif ".jpg" in file and not os.path.exists(path + 'image files/' + file):
        shutil.move(path + file, path + 'image files/' + file)

    elif ".jpeg" in file and not os.path.exists(path + 'image files/' + file):
        shutil.move(path + file, path + 'image files/' + file)

    elif ".cpp" in file and not os.path.exists(path + 'text files/' + file):
        shutil.move(path + file, path + 'text files/' + file)

    elif ".txt" in file and not os.path.exists(path + 'text files/' + file):
        shutil.move(path + file, path + 'text files/' + file)

    elif ".h" in file and not os.path.exists(path + 'text files/' + file):
        shutil.move(path + file, path + 'text files/' + file)

    elif ".png" in file and not os.path.exists(path + 'image files/' + file):
        shutil.move(path + file, path + 'image files/' + file)

    elif ".pdf" in file and not os.path.exists(path + 'document files/' + file):
        shutil.move(path + file, path + 'document files/' + file)

    elif ".docx" in file and not os.path.exists(path + 'document files/' + file):
        shutil.move(path + file, path + 'document files/' + file)

    elif ".pptx" in file and not os.path.exists(path + 'document files/' + file):
        shutil.move(path + file, path + 'document files/' + file)

    elif ".csv" in file and not os.path.exists(path + 'document files/' + file):
        shutil.move(path + file, path + 'document files/' + file)

    elif ".mp4" in file and not os.path.exists(path + 'video files/' + file):
        shutil.move(path + file, path + 'video files/' + file)

    elif ".m4a" in file and not os.path.exists(path + 'audio files/' + file):
        shutil.move(path + file, path + 'audio files/' + file)

    elif ".mp3" in file and not os.path.exists(path + 'audio files/' + file):
        shutil.move(path + file, path + 'audio files/' + file)

    elif ".gif" in file and not os.path.exists(path + 'image files/' + file):
        shutil.move(path + file, path + 'image files/' + file)

    elif ".vrm" in file and not os.path.exists(path + 'misc files/' + file):
        shutil.move(path + file, path + 'misc files/' + file)

    elif ".appxbundle" in file and not os.path.exists(path + 'misc files/' + file):
        shutil.move(path + file, path + 'misc files/' + file)

    elif ".7z" in file and not os.path.exists(path + 'misc files/' + file):
        shutil.move(path + file, path + 'misc files/' + file)

    elif ".ino" in file and not os.path.exists(path + 'text files/' + file):
        shutil.move(path + file, path + 'text files/' + file)

    else:
        print("There were files in this path that were not moved!")
