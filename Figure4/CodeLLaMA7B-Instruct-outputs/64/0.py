

FIX = 

def vowels_count(s):
    
    count = 0
    for char in s:
        if char in 'aeiouy':
            count += 1
    return count

