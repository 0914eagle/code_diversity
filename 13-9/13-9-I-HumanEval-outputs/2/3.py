
from typing import Union, List

def split_words(txt: str) -> Union[List[str], int]:
    
    # check if the input string contains any whitespace
    if ' ' in txt:
        # if it does, split the string on whitespace
        words = txt.split()
    elif ',' in txt:
        # if it doesn't, but the string contains commas, split on commas
        words = txt.split(',')
    else:
        # if the string contains no whitespace or commas, count the number of lower-case letters with odd order in the alphabet
        words = sum(1 for c in txt if c.islower() and ord(c) % 2 == 1)
    return words

