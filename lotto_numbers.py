from itertools import combinations

def lotto_numbers(filename):
    """
    The function "lotto_numbers" generates all possible combinations of 6 numbers from 1 to 49 and
    writes them to a file specified by the "filename" parameter.
    
    :param filename: The filename parameter is the name of the file that will be created to store the
    generated lotto numbers
    :return: the filename of the file that was created.
    """
    with open(filename, 'w') as f:
        for combination in combinations(range(1, 50), 6):
            f.write(' '.join(str(n) for n in combination) + '\n')
    return filename
