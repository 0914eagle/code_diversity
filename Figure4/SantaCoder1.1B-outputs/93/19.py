def encode(message):
    
    message = message.lower()
    message = message.replace('a', 'a')
    message = message.replace('e', 'e')
    message = message.replace('i', 'i')
    message = message.replace('o', 'o')
    message = message.replace('u', 'u')
    message = message.replace('y', 'y')
    message = message.replace('A', 'A')
    message = message.replace('E', 'E')
    message = message.replace('I', 'I')
    message = message.replace('O', 'O')
    message = message.replace('U', 'U')
    message = message.replace('Y', 'Y')
    return message

