FIX = 

def vowels_count(s):
    
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    count = 0
    for i in range(len(s)):
        if s[i] in vowels:
            count += 1
    return count

