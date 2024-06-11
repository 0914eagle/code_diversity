def encode(message):
    
    vowels = ['a', 'e', 'i', 'o', 'u']
    message = message.lower()
    for i in range(len(message)):
        if message[i] in vowels:
            message = message[:i] + message[i].upper() + message[i + 1:]
    return message


