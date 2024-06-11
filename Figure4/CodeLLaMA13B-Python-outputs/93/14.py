def encode(message):
    
    vowels = 'aeiou'
    vowels_upper = 'AEIOU'
    vowels_dict = dict(zip(vowels, vowels[2:] + vowels[:2]))
    vowels_dict_upper = dict(zip(vowels_upper, vowels_upper[2:] + vowels_upper[:2]))
    new_message = ''
    for letter in message:
        if letter.isupper():
            if letter in vowels_upper:
                new_message += vowels_dict_upper[letter]
            else:
                new_message += letter.lower()
        else:
            if letter in vowels:
                new_message += vowels_dict[letter]
            else:
                new_message += letter.upper()
    return new_message

