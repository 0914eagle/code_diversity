FIX = 

def vowels_count(s):
    
    return len([c for c in s if c in "aeiouy" and c != "y" or c == s[-1]])


if