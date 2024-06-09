
def is_berlanese(s):
    vowels = ["a", "o", "u", "i", "e"]
    consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
    
    for i in range(len(s)):
        if s[i] in consonants:
            if i == len(s) - 1 or s[i + 1] not in vowels:
                return "NO"
        elif s[i] == "n":
            if i == len(s) - 1 or s[i + 1] in consonants:
                return "NO"
    
    return "YES"

