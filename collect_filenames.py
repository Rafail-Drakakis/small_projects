import glob 
import os

def collect_filenames(extension):
    """
    The function `collect_filenames` collects all filenames with a given extension in the current
    directory and writes them to a file named "filenames.txt".
    
    :param extension: The "extension" parameter is a string that represents the file extension you want
    to collect filenames for. For example, if you pass ".txt" as the extension, the function will
    collect all the filenames of text files in the current working directory
    :return: the name of the file where the list of filenames is written, which is "filenames.txt".
    """
    files = glob.glob(os.path.join(os.getcwd(), f'*{extension}'))
    target_file = "filenames.txt"
    with open(target_file, 'w') as file:
        file.write('\n'.join(files))
    return target_file
