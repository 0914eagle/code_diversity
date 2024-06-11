

def select_words(s, n):
    
    # Split the input string into a list of words
    words = s.split()
    # Initialize an empty list to store the selected words
    selected_words = []
    # Iterate over the words in the list
    for word in words:
        # Check if the word contains exactly n consonants
        if len([c for c in word if c.isalpha() and not c.isalpha()]) == n:
            # If it does, add it to the selected words list
            selected_words.append(word)
    # Return the selected words list
    return selected_words

