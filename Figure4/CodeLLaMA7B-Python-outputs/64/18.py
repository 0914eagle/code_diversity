FIX = 

def vowels_count(s):
    
    vowels = set("aeiouy")
    return sum(c in vowels for c in s)


