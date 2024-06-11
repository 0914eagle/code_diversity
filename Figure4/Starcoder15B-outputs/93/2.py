def encode(message):
    
    vowels = 'aeiou'
    vowels_dict = {vowel: vowels[(vowels.index(vowel) + 2) % 5] for vowel in vowels}
    message = message.lower()
    encoded_message = ''
    for char in message:
        if char in vowels_dict:
            encoded_message += vowels_dict[char]
        else:
            encoded_message += char.swapcase()
    return encoded_message

