FIX = 

def vowels_count(s):
    
    vowels = "aeiouy"
    count = 0
    for i in s:
        if i in vowels:
            count += 1
    return count


