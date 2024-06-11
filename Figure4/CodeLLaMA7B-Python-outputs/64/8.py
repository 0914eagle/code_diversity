FIX = 

def vowels_count(s):
    
    vowels = {'a', 'e', 'i', 'o', 'u', 'y'}
    return sum(s.count(v) for v in vowels)


if