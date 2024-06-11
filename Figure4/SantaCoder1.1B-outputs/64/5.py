FIX = 

def vowels_count(s):
    
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

