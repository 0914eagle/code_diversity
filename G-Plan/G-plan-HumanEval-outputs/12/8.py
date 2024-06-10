
from typing import Union, List

def split_words(txt: str) -> Union[List[str], int]:
    def split_on_whitespace(txt: str) -> List[str]:
        return txt.split()

    def split_on_commas(txt: str) -> List[str]:
        return txt.split(',')

    def count_lowercase_odd_alphabet(txt: str) -> int:
        return sum(1 for char in txt if char.islower() and ord(char) % 2 == 1)

    if ' ' in txt:
        return split_on_whitespace(txt)
    elif ',' in txt:
        return split_on_commas(txt)
    else:
        return count_lowercase_odd_alphabet(txt)

if __name__ == "__main__":
    txt = input().strip()
    result = split_words(txt)
    print(result)
