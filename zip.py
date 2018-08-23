"""Run the EasyInstall command"""

if __name__ == '__main__':
    import os
    import zipfile

    zf = zipfile.ZipFile("myzipfile.zip", "w")
    for dirname, subdirs, files in os.walk(os.getcwd()):
        zf.write(dirname)
        for filename in files:
            zf.write(os.path.join(dirname, filename))
    zf.close()
