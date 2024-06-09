
def is_berlanese(s):
    vowels = ["a", "o", "u", "i", "e"]
    consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
    
    for i in range(len(s) - 1):
        if s[i] in consonants and s[i + 1] not in vowels and s[i] != "n":
            return "NO"
    
    return "YES"

