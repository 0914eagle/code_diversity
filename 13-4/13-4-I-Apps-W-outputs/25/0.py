
vowels = ['a', 'e', 'i', 'o', 'u']
consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

def can_transform(s, t):
    if len(s) != len(t):
        return "No"
    
    for i in range(len(s)):
        if s[i] in vowels and t[i] in vowels:
            continue
        elif s[i] in consonants and t[i] in consonants:
            continue
        else:
            return "No"
    
    return "Yes"

