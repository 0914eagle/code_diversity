
def nimionese(sentence):
    # Split the sentence into words
    words = sentence.split()
    
    # Create a dictionary to map hard consonants to their nearest neighbors
    hard_consonants = {"b": "a", "c": "b", "d": "c", "g": "d", "k": "e", "n": "f", "p": "g", "t": "h"}
    
    # Iterate through each word and convert it to nimionese
    for i in range(len(words)):
        word = words[i]
        
        # Replace the first letter of the word with its nearest neighbor if it is a hard consonant
        if word[0] in hard_consonants:
            words[i] = hard_consonants[word[0]] + word[1:]
        
        # Replace "each" with "dach"
        if word == "each":
            words[i] = "dach"
        
        # Replace hard consonants in subsequent syllables with the same consonant as the first letter
        if len(word) > 1 and word[1] in hard_consonants:
            words[i] = words[i][0] + hard_consonants[word[1]] + words[i][2:]
        
        # Add "ah", "oh", or "uh" to the end of the word if it ends in a hard consonant
        if word[-1] in hard_consonants:
            words[i] = words[i][:-1] + "ah"
    
    # Join the words back into a sentence and return it
    return " ".join(words)

