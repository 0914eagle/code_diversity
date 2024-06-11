FIX = 

def vowels_count(s):
    
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for i in s:
        if i.lower() in vowels:
            count += 1
    return count

