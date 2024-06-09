
from typing import Union, List

def split_words(txt: str) -> Union[List[str], int]:
    if ' ' in txt:
        return txt.split()
    elif ',' in txt:
        return txt.split(',')
    else:
        count = sum(1 for char in txt if char.islower() and ord(char) % 2 != 0)
        return count

# Test cases
print(split_words('Hello world!'))  # Output: ['Hello', 'world!']
print(split_words('Hello,world!'))  # Output: ['Hello', 'world!']
print(split_words('abcdef'))  # Output: 3
