
def solve(s):
    # Check if the string is empty
    if not s:
        return "NET"
    
    # Check if the string contains only 0s and 1s
    if not s.isdigit():
        return "NET"
    
    # Check if the string is of even length
    if len(s) % 2 == 1:
        return "NET"
    
    # Check if the string can be divided into two equal parts
    if len(s) // 2 != len(set(s)) // 2:
        return "NET"
    
    # Check if the string can be divided into two equal parts with no adjacent characters being the same
    if any(s[i] == s[i+1] for i in range(len(s) - 1)):
        return "NET"
    
    # If all the checks pass, return "DA"
    return "DA"

