
def is_berlanese(s):
    vowels = ["a", "o", "u", "i", "e"]
    consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
    
    if len(s) == 0:
        return "YES"
    
    if s[0] in vowels:
        return is_berlanese(s[1:])
    
    if s[0] == "n":
        if len(s) == 1:
            return "YES"
        else:
            return is_berlanese(s[1:])
    
    if s[0] in consonants:
        if len(s) == 1:
            return "NO"
        else:
            if s[1] in vowels:
                return is_berlanese(s[2:])
            else:
                return "NO"
    
    return "NO"

