
def nimionese(sentence):
    # Split the sentence into words
    words = sentence.split()
    
    # Create a dictionary to map hard consonants to their nearest neighbors
    hard_consonants = {"b": "a", "c": "b", "d": "c", "g": "d", "k": "e", "n": "f", "p": "g", "t": "h"}
    
    # Iterate through the words and translate them to nimionese
    nimionese_words = []
    for word in words:
        # Replace the first letter with the nearest hard consonant
        word = word.replace(word[0], hard_consonants[word[0]])
        
        # Replace "each" with "dach"
        word = word.replace("each", "dach")
        
        # Replace hard consonants in subsequent syllables with the same consonant as the first letter
        word = word.replace(word[1], word[0])
        
        # Add "ah", "oh", or "uh" to the end of the word, whichever is nearest to "a"
        if word[-1] in ["b", "c", "d", "g", "k", "n", "p", "t"]:
            word += "ah"
        elif word[-1] in ["f", "h", "j", "l", "m", "r", "s", "v", "w", "x", "y", "z"]:
            word += "oh"
        else:
            word += "uh"
        
        nimionese_words.append(word)
    
    # Return the translated sentence
    return " ".join(nimionese_words)

