
def split_words(txt: str) -> Union[List[str], int]:
    if ' ' in txt:
        return txt.split()
    elif ',' in txt:
        return txt.split(',')
    else:
        count = sum(1 for char in txt if char.islower() and ord(char) % 2 != 0)
        return count
