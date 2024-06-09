
def nimionese(sentence):
    # Split the sentence into a list of words
    words = sentence.split()
    
    # Create a dictionary to map hard consonants to their nearest neighbors
    hard_consonants = {"b": "a", "c": "b", "d": "c", "g": "d", "k": "g", "n": "k", "p": "n", "t": "p"}
    
    # Iterate through the words and translate them to nimionese
    nimionese_words = []
    for word in words:
        # Check if the word is "each"
        if word == "each":
            nimionese_words.append("Dach")
            continue
        
        # Check if the word starts with a hard consonant
        if word[0] in hard_consonants:
            # Replace the first letter with the nearest hard consonant
            word = hard_consonants[word[0]] + word[1:]
        
        # Check if the word contains a hard consonant in the middle
        if any(c in hard_consonants for c in word[1:]):
            # Replace each hard consonant in the middle with the nearest hard consonant
            for i in range(1, len(word)):
                if word[i] in hard_consonants:
                    word = word[:i] + hard_consonants[word[i]] + word[i+1:]
        
        # Add an 'ah', 'oh', or 'uh' at the end of the word
        if word[-1] in ["b", "c", "d", "g", "k", "n", "p", "t"]:
            word += "ah"
        elif word[-1] == "h":
            word += "uh"
        else:
            word += "oh"
        
        nimionese_words.append(word)
    
    # Return the translated sentence
    return " ".join(nimionese_words)

