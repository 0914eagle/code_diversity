
def weight_of_words(l, w):
    # Initialize a list of letters and their corresponding weights
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
    
    # Initialize a dictionary to store the words and their weights
    word_weights = {}
    
    # Iterate through the letters and calculate the weight of each word
    for letter in letters:
        for i in range(l):
            word = letter * (i + 1)
            word_weights[word] = sum(weights[ord(c) - ord('a')] for c in word)
    
    # Find the word with the given weight
    for word, weight in word_weights.items():
        if weight == w:
            return word
    
    # If no word with the given weight is found, return "impossible"
    return "impossible"

