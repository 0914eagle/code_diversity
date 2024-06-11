def encode(message):
    
    vowels = 'aeiou'
    vowels_upper = 'AEIOU'
    vowels_dict = dict(zip(vowels, vowels[2:] + vowels[:2]))
    vowels_dict_upper = dict(zip(vowels_upper, vowels_upper[2:] + vowels_upper[:2]))
    vowels_dict.update(vowels_dict_upper)
    return ''.join(vowels_dict.get(c, c.upper()) or c.lower() for c in message)


