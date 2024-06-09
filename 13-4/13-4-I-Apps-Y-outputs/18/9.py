
def nimionese(sentence):
    # Split the sentence into a list of words
    words = sentence.split()
    
    # Create a dictionary to map hard consonants to their nearest neighbors
    hard_consonants = {"b": "a", "c": "b", "d": "c", "g": "d", "k": "e", "n": "f", "p": "g", "t": "h"}
    
    # Iterate through the words and convert them to nimionese
    for i in range(len(words)):
        word = words[i]
        
        # Replace the first letter with the nearest hard consonant
        if word[0] in hard_consonants:
            word = hard_consonants[word[0]] + word[1:]
        
        # Replace "each" with "dach"
        if word == "each":
            word = "dach"
        
        # Replace hard consonants in subsequent syllables with the same consonant as the first letter
        if len(word) > 1 and word[1] in hard_consonants:
            word = word[0] + hard_consonants[word[1]] + word[2:]
        
        # Add an "ah", "oh", or "uh" to the end of the word, whichever is nearest to "a"
        if word[-1] in "bcdfghjklmnpqrstvwxyz":
            if word[-1] in "bcdfghjklmnpqrstvwxyz":
                if word[-1] in "bcdfghjklmnpqrstvwxyz":
                    if word[-1] in "bcdfghjklmnpqrstvwxyz":
                        if word[-1] in "bcdfghjklmnpqrstvwxyz":
                            word = word + "ah"
                        else:
                            word = word + "uh"
                    else:
                        word = word + "uh"
                else:
                    word = word + "oh"
            else:
                word = word + "ah"
        
        # Replace "hip-po" with "gip-go"
        if word == "hip-po":
            word = "gip-go"
        
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

