
def is_happy(s: str) -> bool:
    if len(s) < 3:
        return False
    
    for i in range(len(s) - 2):
        window = set(s[i:i+3])
        if len(window) < 3:
            return False
    
    return True

# Test the function with provided examples
print(is_happy('a'))
print(is_happy('aa'))
print(is_happy('abcd'))
print(is_happy('aabb'))
print(is_happy('adb'))
print(is_happy('xyy'))
