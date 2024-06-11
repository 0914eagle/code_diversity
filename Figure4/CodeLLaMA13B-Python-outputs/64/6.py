FIX = 

def vowels_count(s):
    
    vowels = "aeiou"
    count = 0
    for c in s:
        if c in vowels:
            count += 1
        elif c == 'y' and s[-1] == c:
            count += 1
    return count


