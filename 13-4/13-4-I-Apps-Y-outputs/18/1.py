
def nimionese(sentence):
    # Split the sentence into words
    words = sentence.split()
    
    # Create a dictionary to map each word to its nimionese equivalent
    word_map = {
        "cat": "cata",
        "dog": "dogah",
        "hip": "gipoh",
        "each": "dach",
        "hip-po": "gip-go"
    }
    
    # Iterate through each word in the sentence
    for i in range(len(words)):
        # Check if the word is in the dictionary
        if words[i] in word_map:
            # If it is, replace it with its nimionese equivalent
            words[i] = word_map[words[i]]
        else:
            # If it's not, apply the rules to convert it to nimionese
            words[i] = convert_word(words[i])
    
    # Join the words back into a sentence and return it
    return " ".join(words)

def convert_word(word):
    # If the word starts with a hard consonant, replace it with the nearest hard consonant to 'a'
    if word[0] in ["b", "c", "d", "g", "k", "n", "p", "t"]:
        word = "a" + word[1:]
    
    # If the word contains a hard consonant in a subsequent syllable, replace it with the same consonant as the one at the start of the word
    if "h" in word:
        word = word.replace("h", word[0])
    
    # If the word ends in a hard consonant, add an 'ah', 'oh' or 'uh' at the end, rounding towards 'a' in the case of a tie
    if word[-1] in ["b", "c", "d", "g", "k", "n", "p", "t"]:
        if word[-1] == "b":
            word += "ah"
        elif word[-1] == "c":
            word += "oh"
        else:
            word += "uh"
    
    return word

