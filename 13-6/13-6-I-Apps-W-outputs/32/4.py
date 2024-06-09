
def is_berlanese(s):
    vowels = ["a", "o", "u", "i", "e"]
    consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
    
    if len(s) == 0:
        return "YES"
    
    if s[0] in vowels:
        return "YES"
    
    for i in range(1, len(s)):
        if s[i] in consonants and s[i-1] not in vowels:
            return "NO"
        if s[i] == "n" and s[i-1] not in vowels and (i == len(s)-1 or s[i+1] not in vowels):
            return "NO"
    
    return "YES"

