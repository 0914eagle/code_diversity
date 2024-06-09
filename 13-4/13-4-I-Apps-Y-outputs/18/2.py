
def nimionese(sentence):
    # Split the sentence into a list of words
    words = sentence.split()
    
    # Create a dictionary to map each word to its nimionese translation
    nimionese_dict = {
        "cat": "cata",
        "dog": "dogah",
        "hip": "gipoh",
        "each": "dach",
        "hip-po": "gip-go"
    }
    
    # Iterate through the words and translate each one to nimionese
    translated_words = []
    for word in words:
        # Check if the word is already in the dictionary
        if word in nimionese_dict:
            translated_words.append(nimionese_dict[word])
        else:
            # If the word is not in the dictionary, translate it according to the rules
            translated_word = ""
            if word[0] in ["b", "c", "d", "g", "k", "n", "p", "t"]:
                translated_word += "g"
            translated_word += word[1:]
            if translated_word[-1] in ["b", "c", "d", "g", "k", "n", "p", "t"]:
                translated_word += "ah"
            translated_words.append(translated_word)
    
    # Join the translated words into a single string and return it
    return " ".join(translated_words)

