import os
import re

def folderCheck(path):
    # returns true if specified path points to folder
    # returns false if path points to anything else
    if os.path.isdir(path):
        return True
    elif os.path.isfile(path):
        return False
    return False

def openFolder(folder_path):
    # take path to a folder, iterate through it
    # return a list containing the path to all files with the .mp3 extention
    out = []
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".mp3"):
                out.append(os.path.join(root, file))
        return out

def has(filepath):
    return os.path.exists(filepath)

def numerate(filepath):
    # Split the filepath into its directory and filename parts
    # Extract the base filename and extension
    # Use regular expression to find the number in parentheses (if any)
    # If a number in parentheses is found, increment it by 1
    # If no number in parentheses is found, add '(2)' before the file extension
    # Create the updated filepath by combining the directory, new base filename, and extension
    directory, filename = os.path.split(filepath)
    oFname, file_extension = os.path.splitext(filename)
    match = re.search(r'\((\d+)\)', oFname)

    if match:
        newFname = re.sub(r'\(\d+\)', f'({int(match.group(1)) + 1})', oFname)
    else:
        newFname = f'{oFname}(2)'

    return os.path.join(directory, f'{newFname}{file_extension}')

def numerateFiles(path:str):
    # this is the first recursive function i've written in a long time, and the first i've come up with myself
    # generate next filename
    # check if it exists
    # if it does, update s to be next and call function on new s
    # return the next uncreated path
    next = numerate(path)
    if(has(next)):
        path = next
        numerateFiles(path)
    return numerate(next)
