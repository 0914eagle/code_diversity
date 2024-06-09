
def nimionese(sentence):
    # Split the sentence into a list of words
    words = sentence.split()
    
    # Create a dictionary to map hard consonants to their nearest equivalent
    hard_consonants = {"b": "a", "c": "a", "d": "a", "g": "a", "k": "a", "n": "a", "p": "a", "t": "a"}
    
    # Iterate through the words and convert them to nimionese
    for i in range(len(words)):
        word = words[i]
        
        # Convert the first letter of the word to its nearest equivalent
        if word[0] in hard_consonants:
            word = hard_consonants[word[0]] + word[1:]
        
        # Replace "each" with "dach"
        if word == "each":
            word = "dach"
        
        # Replace hard consonants in subsequent syllables with the same consonant as the first letter
        if len(word) > 1 and word[1] in hard_consonants:
            word = word[0] + hard_consonants[word[1]] + word[2:]
        
        # Replace "hip-po" with "gip-go"
        if word == "hip-po":
            word = "gip-go"
        
        # Add an "ah", "oh", or "uh" to the end of the word, whichever is nearest to "a"
        if word[-1] in ["b", "c", "d", "g", "k", "n", "p", "t"]:
            if word[-1] == "b":
                word += "ah"
            elif word[-1] == "c":
                word += "oh"
            elif word[-1] == "d":
                word += "uh"
            elif word[-1] == "g":
                word += "ah"
            elif word[-1] == "k":
                word += "ah"
            elif word[-1] == "n":
                word += "ah"
            elif word[-1] == "p":
                word += "ah"
            elif word[-1] == "t":
                word += "ah"
        
        # Replace "dog" with "dogah"
        if word == "dog":
            word = "dogah"
        
        # Replace "hip" with "gipoh"
        if word == "hip":
            word = "gipoh"
        
        # Update the word in the list
        words[i] = word
    
    # Join the words back into a sentence and return it
    return " ".join(words)

