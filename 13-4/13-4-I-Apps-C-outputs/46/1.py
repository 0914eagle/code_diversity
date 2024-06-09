
def decipher_sentence(s, n, dictionary):
    # Initialize a list to store the possible words
    possible_words = []

    # Iterate over each word in the dictionary
    for word in dictionary:
        # Check if the word is a valid subsequence of the sentence
        if all(c in word for c in s):
            # If the word is a valid subsequence, add it to the list of possible words
            possible_words.append(word)

    # If there is only one possible word, return it
    if len(possible_words) == 1:
        return possible_words[0]
    # If there are no possible words, return "impossible"
    elif not possible_words:
        return "impossible"
    # If there are multiple possible words, return "ambiguous"
    else:
        return "ambiguous"

