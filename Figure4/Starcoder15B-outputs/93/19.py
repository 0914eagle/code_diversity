def encode(message):
    
    vowels = 'aeiou'
    vowels_dict = {'a':'c', 'e':'g', 'i':'k', 'o':'q', 'u':'w'}
    message = message.lower()
    encoded_message = ''
    for char in message:
        if char in vowels:
            encoded_message += vowels_dict[char]
        elif char in vowels_dict.values():
            encoded_message += vowels_dict.keys()[vowels_dict.values().index(char)]
        else:
            encoded_message += char.swapcase()
    return encoded_message

