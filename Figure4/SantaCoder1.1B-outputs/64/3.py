FIX = 

def vowels_count(s):
    
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    return sum(1 for vowel in vowels if s.endswith(vowel))

