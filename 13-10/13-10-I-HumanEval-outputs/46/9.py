
def is_happy(s: str) -> bool:
    
    # Check if the length of the string is at least 3
    if len(s) < 3:
        return False
    
    # Check if every 3 consecutive letters are distinct
    for i in range(len(s) - 2):
        if s[i] == s[i + 1] == s[i + 2]:
            return False
    
    # If all conditions are met, the string is happy
    return True

