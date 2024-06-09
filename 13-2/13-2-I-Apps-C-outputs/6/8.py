
def solve(dictionary, message):
    # Initialize an empty list to store the reconstruction
    reconstruction = []

    # Iterate through the dictionary
    for word in dictionary:
        # Check if the word is a prefix of the message
        if message.startswith(word):
            # If it is, add it to the reconstruction
            reconstruction.append(word)
            # Update the message to remove the word
            message = message[len(word):]

    # Return the reconstruction
    return " ".join(reconstruction)

