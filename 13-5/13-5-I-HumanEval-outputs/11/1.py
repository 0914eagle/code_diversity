
def vowels_count(s: str) -> int:
    
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for char in s:
        if char.lower() in vowels:
            count += 1
    if s.endswith('y') and s[-2].isalpha():
        count -= 1
    return count

