
vowels = set('aeiou')

def can_transform(s, t):
    if len(s) != len(t):
        return "No"
    
    for i in range(len(s)):
        if s[i] in vowels and t[i] not in vowels:
            return "No"
        if s[i] not in vowels and t[i] in vowels:
            return "No"
    
    return "Yes"

