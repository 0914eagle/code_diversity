
def solve(s):
    if len(s) % 2 == 1:
        return "NET"
    
    for i in range(len(s) // 2):
        if s[2 * i] != s[2 * i + 1]:
            return "DA"
    
    return "NET"

