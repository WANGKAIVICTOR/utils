# utils
This python code contains some useful utils, such as  processing the files' names which can be directly used to import files to Logseq. The detailed information is as following.

# Functions
## getAllfielsPathInDir(path)
**Description**: This function is used to get all files path in a directory.  
```  
    Args:  
        path: The directory of files/dirs you want to import.  

    Returns:  
        list contains all files' paths.   
```

## bulkImportFilesToLogseq(path)
**Description**: This function is used to process the file paths, so that they can be imported to the Logseq.
```
    Args:
        path: The directory of files/dirs you want to import.

    Returns:
        None, just print them in the console.
```

## copyAllFilesToNewDir(current_path, dest_path, suffix='.pdf')
**Description**: This function is used to copy all the files with given suffix in a folder to another folder.
```
    Args:
        current_path: The given path of the folder you want to copy from
        dest_path: The folder you want to copy to
        suffix: The file suffix you want to copy

    return:
        None, just print them in the console.
```
