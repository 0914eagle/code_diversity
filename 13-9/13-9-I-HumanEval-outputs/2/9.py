
from typing import Union, List

def split_words(txt: str) -> Union[List[str], int]:
    
    # check if the string contains any whitespace
    if ' ' in txt:
        return txt.split()
    # check if the string contains any commas
    elif ',' in txt:
        return txt.split(',')
    # if the string contains only lower-case letters, return the number of letters with odd order in the alphabet
    elif all(chr.islower() for chr in txt):
        return sum(1 for i, chr in enumerate(txt) if i % 2 == 1)
    # if the string contains any other character, return 0
    else:
        return 0

