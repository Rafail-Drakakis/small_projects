import requests

def get_fact(number):
    """
    The function `get_fact` retrieves a fact about a given number from an API and returns it as a
    string.
    
    :param number: The `number` parameter is the number for which you want to retrieve a fact. It is
    used to construct the URL for the API request
    :return: The function `get_fact` returns the fact about the given number obtained from the
    numbersapi.com API.
    """
    url = "http://numbersapi.com/{}".format(number)
    r = requests.get(url)
    if r.status_code == 200:
        return r.text
    else: 
        print("An error occurred, code={}".format(r.status_code))
