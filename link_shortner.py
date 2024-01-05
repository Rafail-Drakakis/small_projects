import pyshorteners

def link_shortner(link):
    """
    The function "link_shortner" takes a long URL as input and returns a shortened URL using the
    pyshorteners library.
    
    :param link: The link parameter is the URL that you want to shorten
    :return: a shortened version of the input link using the pyshorteners library.
    """
    return pyshorteners.Shortener().tinyurl.short(link)
