
def strlen(string: str) -> int:
    length = 0
    for char in string:
        length += 1
    return length

# Test cases
if __name__ == "__main__":
    assert strlen('') == 0
    assert strlen('abc') == 3
