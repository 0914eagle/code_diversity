
def can_transform(s, t):
    vowels = set("aeiou")
    consonants = set("abcdefghijklmnopqrstuvwxyz") - vowels
    s_vowels = {i for i, c in enumerate(s) if c in vowels}
    s_consonants = {i for i, c in enumerate(s) if c in consonants}
    t_vowels = {i for i, c in enumerate(t) if c in vowels}
    t_consonants = {i for i, c in enumerate(t) if c in consonants}
    return s_vowels == t_vowels and s_consonants == t_consonants

