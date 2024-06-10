
def strlen(string: str) -> int:
    length = 0
    for char in string:
        length += 1
    return length

# Test cases
if __name__ == "__main__":
    input_string = input().strip()
    print(strlen(input_string))
