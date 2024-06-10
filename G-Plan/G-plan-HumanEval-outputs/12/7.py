
def is_happy(s: str) -> bool:
    if len(s) < 3:
        return False
    
    for i in range(len(s) - 2):
        if len(set(s[i:i+3])) < 3:
            return False
    
    return True

# Test cases
if __name__ == "__main__":
    test_cases = ['a', 'aa', 'abcd', 'aabb', 'adb', 'xyy']
    for test in test_cases:
        print(is_happy(test))
