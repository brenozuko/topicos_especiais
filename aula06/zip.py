import os
import zipfile as zip

path_zip = os.path.join(os.sep, "c:\\", "teste", "output.zip")
path_dir = os.path.join(os.sep, "c:\\", "src")

zf = zip.ZipFile(path_zip, "w")

for dirname, subdirs, files in os.walk(path_dir):
    zf.write(dirname)
    for filename in files:
        zf.write(os.path.join(dirname, filename))

zf.close()
