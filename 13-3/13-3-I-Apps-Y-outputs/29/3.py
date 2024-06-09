
def weight_of_words(l, w):
    # Initialize a list of letters with their corresponding weights
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]

    # Create a dictionary to map letters to their weights
    letter_weights = dict(zip(letters, weights))

    # Initialize a list to store the words that match the given length and weight
    words = []

    # Iterate through the dictionary of letters and their weights
    for letter, weight in letter_weights.items():
        # Check if the current weight is less than or equal to the given weight
        if weight <= w:
            # If the current weight is equal to the given weight, add the current letter to the list of words
            if weight == w:
                words.append(letter)
            # If the current weight is less than the given weight, recursively call the function to find the remaining weight
            else:
                remaining_weight = w - weight
                remaining_words = weight_of_words(l - 1, remaining_weight)
                for word in remaining_words:
                    words.append(letter + word)

    # If no words are found, return "impossible"
    if not words:
        return "impossible"
    # Otherwise, return the first word in the list
    else:
        return words[0]

