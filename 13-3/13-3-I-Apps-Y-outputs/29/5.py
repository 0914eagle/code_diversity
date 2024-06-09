
def weight_of_words(l, w):
    # Initialize a list of letters with their corresponding weights
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]

    # Initialize a dictionary to store the possible words
    words = {}

    # Iterate through the letters and their weights
    for letter, weight in zip(letters, weights):
        # If the weight of the letter is less than or equal to the given weight, add it to the dictionary
        if weight <= w:
            words[letter] = weight

    # Initialize an empty string to store the final word
    word = ""

    # Iterate through the dictionary of possible words
    for letter, weight in words.items():
        # If the weight of the word is equal to the given weight, return the word
        if weight == w:
            return letter
        # If the weight of the word is less than the given weight, add the letter to the word and subtract its weight from the given weight
        elif weight < w:
            word += letter
            w -= weight

    # If no word is found, return "impossible"
    return "impossible"

