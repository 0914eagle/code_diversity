

def select_words(s, n):
    
    # Split the input string into a list of words
    words = s.split()
    # Initialize an empty list to store the selected words
    selected_words = []
    # Iterate over the words in the input string
    for word in words:
        # Check if the word contains the required number of consonants
        if len([c for c in word if c.lower() not in "aeiou"]) == n:
            # If it does, add it to the selected words list
            selected_words.append(word)
    # Return the selected words
    return selected_words


