import os

def merge_files_by_extension(extension):
    """
    The function `merge_files_by_extension` merges all files in the current directory with a given
    extension into a single file.
    
    :param extension: The "extension" parameter is a string that represents the file extension of the
    files you want to merge. For example, if you want to merge all the text files in a directory, you
    would pass ".txt" as the extension parameter
    :return: the name of the merged file.
    """
    merged_file_name = f"merged{extension}"
    files = [file for file in os.listdir() if file.endswith(extension)]

    with open(merged_file_name, "w") as merged_file:
        for file_name in files:
            with open(file_name, "r") as file:
                merged_file.write(f"// {file_name}\n")
                for line in file:
                    merged_file.write(line)
                merged_file.write("\n")

    return merged_file_name
