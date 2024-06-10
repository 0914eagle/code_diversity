
def check_win(s):
    if len(s) == 3:
        return "First"
    
    # Check if the string is valid
    if not is_valid_string(s):
        return "Second"
    
    # Check if Takahashi can win
    if can_takahashi_win(s):
        return "First"
    
    # Check if Aoki can win
    if can_aoki_win(s):
        return "Second"
    
    # If both players cannot win, return "Second"
    return "Second"

def is_valid_string(s):
    # Check if the string is valid
    for i in range(1, len(s) - 1):
        if s[i] == s[i - 1] or s[i] == s[i + 1]:
            return False
    return True

def can_takahashi_win(s):
    # Check if Takahashi can win by removing the first character
    if s[1] != s[0] and s[2] != s[0]:
        return True
    
    # Check if Takahashi can win by removing the last character
    if s[-2] != s[-1] and s[-3] != s[-1]:
        return True
    
    # Check if Takahashi can win by removing the middle character
    if s[1] != s[0] and s[-2] != s[-1]:
        return True
    
    return False

def can_aoki_win(s):
    # Check if Aoki can win by removing the first character
    if s[1] != s[0] and s[2] != s[0]:
        return True
    
    # Check if Aoki can win by removing the last character
    if s[-2] != s[-1] and s[-3] != s[-1]:
        return True
    
    # Check if Aoki can win by removing the middle character
    if s[1] != s[0] and s[-2] != s[-1]:
        return True
    
    return False

if __name__ == '__main__':
    s = input()
    print(check_win(s))

