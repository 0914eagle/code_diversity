
def strlen(string: str) -> int:
    length = 0
    for char in string:
        length += 1
    return length

# Test cases
print(strlen(''))  # 0
print(strlen('abc'))  # 3
