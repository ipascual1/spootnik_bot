from requests import get
from support import extract
import re

URL = "http://randomfactgenerator.net/"

def random_fact():
    """
        returns: A str object with a random fact.
    
    Gets a random fact in HTML from http://randomfactgenerator.net/
    and parses it to a string.
    """
    # Get the HTML and strip the RE
    response = get(URL)
    fact = extract(r"<div id=\\'z\\'>.+?<br/>",
                   "<div id=\\'z\\'>",
                   "<br/>",
                   str(response.content))

    # Minor grammar corrections
    fact_updated = fact.replace(".", "?", 1)
    if fact_updated == fact:
        fact = fact[:-1] + "?"
    else:
        fact = fact_updated
    if fact[0] == " ":
        fact = fact[1:]
    fact = fact[0].lower() + fact[1:]
    return fact
