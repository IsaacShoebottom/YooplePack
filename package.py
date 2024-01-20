import os
import shutil

def main():
    # Files to zip
    files = [
        "manifest.json",
        "README.md",
        "icon.png",
        "BepInEx/"
    ]

    BUILD_DIR = "build/" 

    # Remove build folder if exists
    if os.path.exists(BUILD_DIR):
        shutil.rmtree(BUILD_DIR)
    # Create build folder
    os.mkdir(BUILD_DIR)

    # Copy files to build folder
    for file in files:
        if os.path.isfile(file):
            shutil.copy(file, BUILD_DIR + file)
        else:
            shutil.copytree(file, BUILD_DIR + file)

    # Zip file name
    ZIP_NAME = "YooplePack"

    # Remove zip file if exists
    if os.path.exists(ZIP_NAME + ".zip"):
        os.remove(ZIP_NAME + ".zip")
    # Zip file
    shutil.make_archive(ZIP_NAME, "zip", BUILD_DIR)

    # Remove build folder
    shutil.rmtree(BUILD_DIR)


if __name__ == "__main__":
    main()