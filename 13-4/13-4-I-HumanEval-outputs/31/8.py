
def encode(message: str) -> str:
    
    # Create a list of vowels
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    # Create a list of letters in the message
    message_list = list(message)
    
    # Iterate through the message and encode each letter
    encoded_message = ''
    for letter in message_list:
        # If the letter is a vowel, replace it with the letter that is 2 positions ahead of it in the alphabet
        if letter.lower() in vowels:
            index = vowels.index(letter.lower()) + 2
            if index > 5:
                index = index - 5
            encoded_letter = vowels[index]
        # If the letter is not a vowel, swap its case
        else:
            if letter.islower():
                encoded_letter = letter.upper()
            else:
                encoded_letter = letter.lower()
        # Add the encoded letter to the encoded message
        encoded_message += encoded_letter
    
    return encoded_message

