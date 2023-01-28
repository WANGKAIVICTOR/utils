import os
import sys
import shutil


def getAllfielsPathInDir(path):
    """
    This function is used to get all files path in a directory
    Args:
        path: The directory of files/dirs you want to import.

    Returns:
        list contains all files' paths. 
    """

    if not os.path.exists(path):
        print("Cannot find the file/directory.")
        sys.exit()

    if os.path.isfile(path):
        return [path]

    files = []
    paths = os.listdir(path)
    while len(paths) > 0:
        current_path = paths.pop(0)
        if os.path.isdir(path + '\\' + current_path):
            files += getAllfielsPathInDir(path + '\\' + current_path)
        else:
            files.append(path + '\\' + current_path)
    return files


def bulkImportFilesToLogseq(path):
    """
    This function is used to process the file paths, so that they can be imported to the Logseq.
    Args:
        path: The directory of files/dirs you want to import.

    Returns:
        None, just print them in the console.
    """

    for file in getAllfielsPathInDir(path):
        file_name = file.split('\\')
        print('![' + file_name[-1] + ']' + '(file://' + file + ')')


def copyAllFilesToNewDir(current_path, dest_path, suffix='.pdf'):
    """
    This function is used to copy all the files with given suffix in a folder to another folder.
    Args:
        current_path: The given path of the folder you want to copy from
        dest_path: The folder you want to copy to
        suffix: The file suffix you want to copy

    return:
        None, just print them in the console.
    """

    for file in getAllfielsPathInDir(current_path):
        if file.endswith(suffix):
            shutil.copy(file, dest_path+'\\'+file.split('\\')[-1])
            print(file)
