
def is_nested(string: str) -> bool:
    
    if len(string) % 2 == 1:
        return False
    count = 0
    for char in string:
        if char == '[':
            count += 1
        elif char == ']':
            count -= 1
        if count < 0:
            return False
    return count == 0

