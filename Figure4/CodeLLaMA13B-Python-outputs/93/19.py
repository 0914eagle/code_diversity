def encode(message):
    
    vowels = 'aeiou'
    vowels_dict = {v: vowels[(i+2)%5] for i, v in enumerate(vowels)}
    return ''.join(vowels_dict[c] if c in vowels else c.upper() if c.islower() else c.lower() for c in message)

