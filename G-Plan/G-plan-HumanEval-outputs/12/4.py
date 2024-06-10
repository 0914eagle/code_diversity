
def is_happy(s: str) -> bool:
    if len(s) < 3:
        return False
    
    for i in range(len(s) - 2):
        if s[i] == s[i + 1] or s[i] == s[i + 2] or s[i + 1] == s[i + 2]:
            return False
    
    return True

# Test the function
if __name__ == "__main__":
    test_cases = ['a', 'aa', 'abcd', 'aabb', 'adb', 'xyy']
    for test_case in test_cases:
        print(is_happy(test_case))
