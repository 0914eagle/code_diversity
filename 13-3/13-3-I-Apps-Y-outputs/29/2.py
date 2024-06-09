
def weight_of_words(l, w):
    # Initialize a list of letters and their corresponding weights
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
    
    # Initialize a dictionary to store the weight of each letter
    letter_weights = {}
    for i in range(len(letters)):
        letter_weights[letters[i]] = weights[i]
    
    # Initialize a list to store the possible words
    words = []
    
    # Iterate through the letters and add them to the word if the weight is less than or equal to the given weight
    for letter in letters:
        if letter_weights[letter] <= w:
            words.append(letter)
    
    # If the length of the word is less than the given length, recursively call the function to add more letters
    if len(words) < l:
        return weight_of_words(l, w - letter_weights[words[-1]])
    
    # If the length of the word is equal to the given length, return the word
    elif len(words) == l:
        return ''.join(words)
    
    # If the length of the word is greater than the given length, return impossible
    else:
        return 'impossible'

