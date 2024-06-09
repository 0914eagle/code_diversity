
def distinct_words(s):
    # Initialize a set to store the generated words
    words = set()
    
    # Add the initial word to the set
    words.add(s)
    
    # Loop for each character in the word
    for i in range(len(s)):
        # Generate a new word by moving the last character to the beginning
        new_word = s[i:] + s[:i]
        
        # Add the new word to the set if it's not already present
        if new_word not in words:
            words.add(new_word)
    
    # Return the number of distinct words generated
    return len(words)

