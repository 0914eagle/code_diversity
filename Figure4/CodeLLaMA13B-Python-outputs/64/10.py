FIX = 

def vowels_count(s):
    
    vowels = 'aeiouy'
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count
