
def solve_nvwls(dictionary, message):
    # Initialize an empty list to store the reconstructed sentence
    sentence = []

    # Iterate through the message
    for char in message:
        # If the character is a consonant, append it to the sentence
        if char.isconsonant():
            sentence.append(char)

    # Join the sentence into a string and return it
    return " ".join(sentence)

