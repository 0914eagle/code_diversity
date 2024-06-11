def encode(message):
    
    vowels = 'aeiou'
    vowels_dict = {v: vowels[(i+2)%len(vowels)] for i, v in enumerate(vowels)}
    return ''.join(vowels_dict.get(c, c.lower()) or c.upper() for c in message)

