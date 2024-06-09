
def digitSum(s: str) -> int:
    
    sum = 0
    for c in s:
        if c.isupper():
            sum += ord(c)
    return sum

