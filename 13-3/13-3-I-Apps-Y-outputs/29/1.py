
def weight_of_words(l, w):
    # Initialize a list of letters and their corresponding weights
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
    
    # Initialize a dictionary to store the weight of each letter
    letter_weights = {}
    for i in range(len(letters)):
        letter_weights[letters[i]] = weights[i]
    
    # Initialize a list to store the words of the given length
    words = []
    
    # Iterate through the dictionary of letters and their weights
    for letter in letter_weights:
        # Check if the weight of the letter is less than or equal to the given weight
        if letter_weights[letter] <= w:
            # Add the letter to the list of words
            words.append(letter)
    
    # Check if the length of the list of words is equal to the given length
    if len(words) == l:
        # Return the list of words
        return "".join(words)
    else:
        # Return the string "impossible"
        return "impossible"

