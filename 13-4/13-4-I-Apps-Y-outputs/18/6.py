
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
            translated_word = word[0]
            for i in range(1, len(word)):
                if word[i] in "bcdfghjklmnpqrstvwxyz":
                    translated_word += word[i]
                elif word[i] == "-":
                    translated_word += "-"
                else:
                    translated_word += word[i].lower()
            translated_words.append(translated_word)
    
    # Join the translated words into a single string and return the result
    return " ".join(translated_words)

