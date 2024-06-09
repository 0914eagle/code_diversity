
def nimionese(sentence):
    # Split the sentence into a list of words
    words = sentence.split()
    
    # Create a dictionary to map each word to its nimionese translation
    word_map = {
        "cat": "cata",
        "dog": "doga",
        "hip": "gipoh",
        "each": "dach",
        "hip-po": "gip-go"
    }
    
    # Iterate through the words and translate each one to nimionese
    nimionese_words = []
    for word in words:
        # Check if the word is already in the dictionary
        if word in word_map:
            nimionese_words.append(word_map[word])
        else:
            # If the word is not in the dictionary, translate it according to the rules
            nimionese_word = ""
            if word[0] in ["b", "c", "d", "g", "k", "n", "p", "t"]:
                nimionese_word += "g"
            nimionese_word += word[1:]
            if nimionese_word[-1] in ["b", "c", "d", "g", "k", "n", "p", "t"]:
                nimionese_word += "ah"
            nimionese_words.append(nimionese_word)
    
    # Join the translated words together with spaces and return the result
    return " ".join(nimionese_words)

