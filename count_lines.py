def count_lines(filename):
    """
    The function `count_lines` takes a filename as input and returns the number of lines in the file.
    
    :param filename: The filename parameter is a string that represents the name of the file you want to
    count the lines of
    :return: The function `count_lines` returns the number of lines in the file specified by the
    `filename` parameter.
    """
    with open(filename, 'r') as f:
        lines = f.readlines()
        return len(lines)
