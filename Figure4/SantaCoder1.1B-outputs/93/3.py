def encode(message):
    
    # Your code here
    vowels = 'aeiouAEIOU'
    new_message = ''
    for letter in message:
        if letter.isalpha():
            if letter.lower() in vowels:
                new_message += letter.lower()
            else:
                new_message += letter.upper()
        else:
            new_message += letter
    return new_message

