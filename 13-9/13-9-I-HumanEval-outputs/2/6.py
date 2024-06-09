
from typing import Union, List

def split_words(txt: str) -> Union[List[str], int]:
    
    if ' ' in txt:
        return txt.split()
    elif ',' in txt:
        return txt.split(',')
    else:
        return sum(1 for c in txt.lower() if c.isalpha() and c not in 'aeiou' and ord(c) % 2 == 1)

