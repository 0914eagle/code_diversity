
def solve(s, d):
    # Initialize variables
    correct_translations = 0
    incorrect_translations = 0
    
    # Iterate through each word in the Dutch sentence
    for word in s:
        # Check if the word is in the dictionary
        if word in d:
            # If the word is in the dictionary, check if it is a correct or incorrect translation
            if d[word] == "correct":
                correct_translations += 1
            else:
                incorrect_translations += 1
    
    # Return the number of correct and incorrect translations
    return correct_translations, incorrect_translations

