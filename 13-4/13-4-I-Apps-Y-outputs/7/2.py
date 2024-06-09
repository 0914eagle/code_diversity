
def solve(s, d):
    # Initialize variables
    correct_translations = 0
    incorrect_translations = 0
    possible_translations = []

    # Iterate through each word in the sentence
    for word in s:
        # Check if the word is in the dictionary
        if word in d:
            # If the word is in the dictionary, check if it is a correct or incorrect translation
            if d[word] == "correct":
                correct_translations += 1
            else:
                incorrect_translations += 1
        else:
            # If the word is not in the dictionary, add it to the list of possible translations
            possible_translations.append(word)

    # If there is only one possible translation, return it and its correctness
    if len(possible_translations) == 1:
        return f"{possible_translations[0]}\n{'' if correct_translations == 1 else 'in'}correct"

    # If there are multiple possible translations, return the total number of correct and incorrect translations
    return f"{correct_translations}\n{incorrect_translations}\n"

