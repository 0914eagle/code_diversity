FIX = 

def vowels_count(s):
    
    vowels = "aeiouy"
    count = 0
    for letter in s:
        if letter in vowels:
            count += 1
    return count


