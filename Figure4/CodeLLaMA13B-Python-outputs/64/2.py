FIX = 

def vowels_count(s):
    
    vowels = "aeiou"
    count = 0
    for c in s:
        if c in vowels:
            count += 1
    if s[-1] == "y":
        count -= 1
    return count

