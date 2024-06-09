
def nimionese(sentence):
    # Split the sentence into a list of words
    words = sentence.split()
    
    # Create a dictionary to map each word to its nimionese translation
    word_map = {
        "cat": "cata",
        "hip": "gipoh",
        "dog": "dogah",
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
            nimionese_word = translate_word(word)
            nimionese_words.append(nimionese_word)
    
    # Join the translated words together with spaces and return the result
    return " ".join(nimionese_words)

def translate_word(word):
    # If the word starts with a hard consonant, replace it with the nearest hard consonant to 'a'
    if word[0] in "bcdfghjklmnpqrstvwxyz":
        word = "a" + word[1:]
    
    # If the word contains a dash, replace it with a space
    word = word.replace("-", " ")
    
    # If the word contains a hard consonant other than the first one, replace it with the same consonant as the first one
    if word[1:] != "":
        word = word[0] + word[1:].replace(word[0], "")
    
    # If the word ends with a hard consonant, add an 'ah', 'oh', or 'uh' to the end, whichever is nearest to 'a'
    if word[-1] in "bcdfghjklmnpqrstvwxyz":
        if word[-1] in "bcdfghjklmnpqrstvwxyz":
            word += "ah"
        elif word[-1] in "bcdfghjklmnpqrstvwxyz":
            word += "oh"
        else:
            word += "uh"
    
    return word

