
def can_transform(s, t):
    vowels = set("aeiou")
    consonants = set("abcdefghijklmnopqrstuvwxyz") - vowels
    s_vowels = [c for c in s if c in vowels]
    s_consonants = [c for c in s if c in consonants]
    t_vowels = [c for c in t if c in vowels]
    t_consonants = [c for c in t if c in consonants]
    if len(s_vowels) != len(t_vowels) or len(s_consonants) != len(t_consonants):
        return "No"
    for i in range(len(s_vowels)):
        if s_vowels[i] not in t_vowels:
            return "No"
    for i in range(len(s_consonants)):
        if s_consonants[i] not in t_consonants:
            return "No"
    return "Yes"

