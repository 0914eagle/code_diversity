
def solve(s, d):
    # Initialize variables
    correct_translations = 0
    incorrect_translations = 0
    possible_translations = []

    # Split the Dutch sentence into words
    words = s.split()

    # Loop through each word in the Dutch sentence
    for word in words:
        # Check if the word is in the dictionary
        if word in d:
            # If the word is in the dictionary, check if it has a correct translation
            if d[word] == "correct":
                # If the word has a correct translation, add it to the list of possible translations
                possible_translations.append(word)
            else:
                # If the word has an incorrect translation, add it to the list of possible translations
                possible_translations.append(word)
                incorrect_translations += 1
        else:
            # If the word is not in the dictionary, add it to the list of possible translations
            possible_translations.append(word)
            incorrect_translations += 1

    # Calculate the number of correct translations
    correct_translations = len(possible_translations)

    # Return the number of correct and incorrect translations
    return correct_translations, incorrect_translations

