def encode(message):
    
    vowels = 'aeiou'
    vowels_dict = {'a':'c', 'e':'g', 'i':'k', 'o':'q', 'u':'w'}
    message = message.lower()
    encoded_message = ''
    for letter in message:
        if letter in vowels:
            encoded_message += vowels_dict[letter]
        elif letter == ' ':
            encoded_message += ' '
        else:
            encoded_message += letter.swapcase()
    return encoded_message

