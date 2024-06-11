FIX = 

def vowels_count(s):
    
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    count = 0
    for letter in s:
        if letter in vowels:
            count += 1
    return count

