
def weight_of_words(l, w):
    # Initialize a list of weights for each letter
    weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
    
    # Initialize an empty string to store the word
    word = ""
    
    # Iterate through the possible letters
    for i in range(1, 27):
        # If the weight of the current letter is less than or equal to the given weight, append it to the word
        if weights[i-1] <= w:
            word += chr(i+96)
            w -= weights[i-1]
        
        # If the length of the word is equal to the given length, return the word
        if len(word) == l:
            return word
    
    # If no word can be found, return "impossible"
    return "impossible"

