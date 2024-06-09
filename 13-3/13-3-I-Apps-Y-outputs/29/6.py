
def weight_of_words(l, w):
    # Initialize a list of weights for each letter of the alphabet
    weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
    
    # Initialize an empty string to store the word
    word = ""
    
    # Iterate through the length of the word
    for i in range(l):
        # Iterate through the alphabet
        for j in range(26):
            # If the weight of the letter is less than or equal to the remaining weight, add it to the word and decrease the remaining weight
            if weights[j] <= w:
                word += chr(j + 97)
                w -= weights[j]
                break
    
    # If the word is empty, return "impossible"
    if not word:
        return "impossible"
    
    # Return the word
    return word

