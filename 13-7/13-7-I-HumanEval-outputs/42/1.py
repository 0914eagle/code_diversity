
def digitSum(s: str) -> int:
    
    upper_chars = [c for c in s if c.isupper()]
    return sum([ord(c) for c in upper_chars])

