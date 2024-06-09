
def decipher_sentence(s, n, dictionary):
    # Initialize a set to store the unique words
    unique_words = set()

    # Iterate through the dictionary and add each word to the set
    for word in dictionary:
        unique_words.add(word)

    # Initialize a list to store the deciphered sentence
    deciphered_sentence = []

    # Iterate through the input sentence and check if each word is in the dictionary
    for word in s.split():
        if word in unique_words:
            deciphered_sentence.append(word)
        else:
            return "impossible"

    # If all words are in the dictionary, return the deciphered sentence
    if len(deciphered_sentence) == len(s.split()):
        return " ".join(deciphered_sentence)

    # If not all words are in the dictionary, return "ambiguous"
    return "ambiguous"

