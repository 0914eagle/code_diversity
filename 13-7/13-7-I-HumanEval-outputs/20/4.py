
def is_nested(string: str) -> bool:
    
    if len(string) % 2 == 1:
        return False
    count = 0
    for i in range(len(string)):
        if string[i] == '[':
            count += 1
        else:
            count -= 1
        if count < 0:
            return False
    return count == 0

