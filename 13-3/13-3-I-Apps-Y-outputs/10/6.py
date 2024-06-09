
def f1(s, d):
    # Initialize variables
    n = len(s)
    m = len(d)
    correct_translations = 0
    incorrect_translations = 0
    
    # Iterate through each word in the sentence
    for i in range(n):
        # Check if the word is in the dictionary
        if s[i] in d:
            # If the word is in the dictionary, check if it is a correct translation
            if d[s[i]] == "correct":
                correct_translations += 1
            else:
                incorrect_translations += 1
    
    # Return the number of correct and incorrect translations
    return correct_translations, incorrect_translations

def f2(s, d):
    # Initialize variables
    n = len(s)
    m = len(d)
    correct_translations = 0
    incorrect_translations = 0
    
    # Iterate through each word in the sentence
    for i in range(n):
        # Check if the word is in the dictionary
        if s[i] in d:
            # If the word is in the dictionary, check if it is a correct translation
            if d[s[i]] == "correct":
                correct_translations += 1
            else:
                incorrect_translations += 1
    
    # Return the number of correct and incorrect translations
    return correct_translations, incorrect_translations

if __name__ == '__main__':
    s = input()
    d = input()
    correct_translations, incorrect_translations = f1(s, d)
    print(correct_translations, "correct")
    print(incorrect_translations, "incorrect")

