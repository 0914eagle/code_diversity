
from typing import Union, List

def split_words(txt: str) -> Union[List[str], int]:
    if ' ' in txt:
        return txt.split()
    elif ',' in txt:
        return txt.split(',')
    else:
        return count_odd_lower_letters(txt)

def count_odd_lower_letters(txt: str) -> int:
    return sum(1 for char in txt if char.islower() and ord(char) % 2 == 1)

if __name__ == "__main__":
    txt = input().strip()
    result = split_words(txt)
    print(result)
