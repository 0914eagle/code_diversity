
def vowels_count(s: str) -> int:
    
    vowels = set('aeiouy')
    count = 0
    for char in s:
        if char.lower() in vowels:
            count += 1
    return count

