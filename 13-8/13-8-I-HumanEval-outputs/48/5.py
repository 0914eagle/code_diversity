
def solve(s: str) -> str:
    
    # reverse the string if it contains no letters
    if not any(c.isalpha() for c in s):
        return s[::-1]
    
    # reverse the case of each letter
    result = ''
    for c in s:
        if c.isalpha():
            result += c.swapcase()
        else:
            result += c
    return result

