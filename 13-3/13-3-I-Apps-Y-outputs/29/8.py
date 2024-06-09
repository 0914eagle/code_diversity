
def weight_of_words(l, w):
    # Initialize a list of all lowercase English letters
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    # Initialize a dictionary to map each letter to its weight
    letter_weights = {letter: i for i, letter in enumerate(letters, start=1)}
    
    # Initialize a list to store all possible words of length l
    words = []
    
    # Iterate over all possible combinations of letters of length l
    for combination in itertools.combinations(letters, l):
        # Convert the combination to a string
        word = ''.join(combination)
        
        # Calculate the weight of the word
        weight = sum(letter_weights[letter] for letter in word)
        
        # If the weight is equal to w, add the word to the list of possible words
        if weight == w:
            words.append(word)
    
    # If no words were found, return "impossible"
    if not words:
        return "impossible"
    
    # Otherwise, return any of the possible words
    return words[0]

