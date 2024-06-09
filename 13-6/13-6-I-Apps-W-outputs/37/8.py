
def solve(s):
    # Check if the string is empty
    if not s:
        return "NET"
    
    # Check if the string contains only 0s and 1s
    if not s.isdigit():
        return "NET"
    
    # Check if the string is a power of 2
    if bin(int(s, 2)).count("1") != 1:
        return "NET"
    
    # Check if the string can be divided into two equal parts
    if len(s) % 2 != 0:
        return "NET"
    
    # Check if the first half of the string is equal to the second half
    if s[:len(s)//2] != s[len(s)//2:]:
        return "NET"
    
    # If all the checks pass, return "DA"
    return "DA"

