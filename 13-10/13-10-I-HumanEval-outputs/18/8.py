
def count_upper(s: str) -> int:
    
    count = 0
    for i in range(len(s)):
        if s[i].isupper() and i % 2 == 0:
            count += 1
    return count

