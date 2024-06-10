
def strlen(string: str) -> int:
    length = 0
    for char in string:
        length += 1
    return length

input_string = input()
print(strlen(input_string))
