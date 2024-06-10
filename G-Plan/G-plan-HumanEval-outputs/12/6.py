
from typing import Union, List

def split_words(txt: str) -> Union[List[str], int]:
    def split_on_whitespace(text: str) -> List[str]:
        return text.split()

    def split_on_commas(text: str) -> List[str]:
        return text.split(',')

    def count_odd_lowercase_letters(text: str) -> int:
        return sum(1 for char in text if char.islower() and ord(char) % 2 == 1)

    if ' ' in txt:
        return split_on_whitespace(txt)
    elif ',' in txt:
        return split_on_commas(txt)
    else:
        return count_odd_lowercase_letters(txt)

if __name__ == "__main__":
    txt = input().strip()
    result = split_words(txt)
    print(result)
