
from typing import Union, List

def split_words(txt: str) -> Union[List[str], int]:
    
    # Split the text on whitespace
    words = txt.split()
    
    # If there are no words, try splitting on commas
    if len(words) == 0:
        words = txt.split(',')
    
    # If there are still no words, return the number of lower-case letters with odd order in the alphabet
    if len(words) == 0:
        return sum(1 for c in txt.lower() if c.isalpha() and ord(c) % 2 == 1)
    
    # Otherwise, return the list of words
    return words

