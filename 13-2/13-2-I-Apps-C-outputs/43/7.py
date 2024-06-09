
def solve_nvwls(dictionary, message):
    # Initialize an empty list to store the reconstructed sentence
    sentence = []

    # Iterate through the message
    for char in message:
        # If the character is a consonant, append it to the sentence
        if char.isconsonant():
            sentence.append(char)
        # If the character is a space, append a space to the sentence
        elif char.isspace():
            sentence.append(" ")

    # Join the list of characters to form the reconstructed sentence
    reconstructed_sentence = "".join(sentence)

    # Return the reconstructed sentence
    return reconstructed_sentence

