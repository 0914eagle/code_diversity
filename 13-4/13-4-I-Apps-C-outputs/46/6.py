
def decipher_sentence(s, n, dictionary):
    # Initialize a set to store the unique words
    unique_words = set()

    # Iterate over the dictionary
    for word in dictionary:
        # Check if the word is a substring of the sentence
        if word in s:
            # Add the word to the set of unique words
            unique_words.add(word)

    # Check if the set of unique words is equal to the number of words in the dictionary
    if len(unique_words) == n:
        # Sort the unique words in alphabetical order
        unique_words = sorted(unique_words)
        # Join the unique words to form the deciphered sentence
        deciphered_sentence = " ".join(unique_words)
        return deciphered_sentence
    else:
        return "impossible"

