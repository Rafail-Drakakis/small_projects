def count_words(filename):
    """
    The function `count_words` takes a filename as input, reads the file, counts the occurrences of each
    word, and returns a dictionary with the word counts.
    
    :param filename: The `filename` parameter is a string that represents the name of the file that you
    want to count the words in
    :return: a dictionary containing the counts of each word in the file.
    """
    with open(filename, "r") as f:
        all_words = []
        for line in f:
            all_words.extend(line.split())  
        word_counts = {}
        first_occurrences = {}
        for i, word in enumerate(all_words):
            if word not in word_counts:
                word_counts[word] = 1
                first_occurrences[word] = i
            else:
                word_counts[word] += 1
        return word_counts
