

def select_words(s, n):
    
    # Split the input string into a list of words
    words = s.split()
    # Initialize an empty list to store the selected words
    selected_words = []
    # Iterate over the words in the list
    for word in words:
        # Check if the word contains the required number of consonants
        if len([c for c in word if c.lower() not in "aeiou"]) == n:
            selected_words.append(word)
    # Return the list of selected words
    return selected_words


