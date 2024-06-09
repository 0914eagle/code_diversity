
from typing import Union, List

def split_words(txt: str) -> Union[List[str], int]:
    
    txt = txt.lower()
    if ' ' in txt:
        return txt.split()
    elif ',' in txt:
        return txt.split(',')
    else:
        return sum(1 for i in txt if i.isalpha() and ord(i) % 2 == 1)

