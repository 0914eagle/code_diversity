
def can_transform(s, t):
    vowels = set("aeiou")
    consonants = set("bcdfghjklmnpqrstvwxyz")
    s_vowels = {c for c in s if c in vowels}
    s_consonants = {c for c in s if c in consonants}
    t_vowels = {c for c in t if c in vowels}
    t_consonants = {c for c in t if c in consonants}
    return s_vowels == t_vowels and s_consonants == t_consonants

