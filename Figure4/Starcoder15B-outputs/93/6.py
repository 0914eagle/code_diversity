def encode(message):
    
    vowels = 'aeiou'
    vowels_dict = {vowel: vowels[(vowels.index(vowel) + 2) % 5] for vowel in vowels}
    encoded = ''
    for char in message:
        if char.lower() in vowels_dict:
            encoded += vowels_dict[char.lower()]
        else:
            encoded += char.swapcase()
    return encoded

