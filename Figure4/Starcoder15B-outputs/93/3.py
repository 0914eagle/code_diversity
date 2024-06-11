def encode(message):
    
    vowels = 'aeiou'
    vowels_dict = {vowel: vowels[(vowels.index(vowel) + 2) % 5] for vowel in vowels}
    encoded_message = ''
    for char in message:
        if char.isalpha():
            if char.islower():
                encoded_message += char.upper() if char in vowels_dict else char.swapcase()
            else:
                encoded_message += char.lower() if char in vowels_dict else char.swapcase()
        else:
            encoded_message += char
    return encoded_message


