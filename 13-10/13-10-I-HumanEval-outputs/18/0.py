
def count_upper(s: str) -> int:
    
    count = 0
    for i in range(0, len(s), 2):
        if s[i].isupper() and s[i].lower() in 'aeiou':
            count += 1
    return count

