
def split_words(txt: str) -> Union[List[str], int]:
    words = txt.split()
    if len(words) > 1:
        return words
    elif ',' in txt:
        return txt.split(',')
    else:
        count = sum(1 for char in txt if char.islower() and ord(char) % 2 != 0)
        return count
