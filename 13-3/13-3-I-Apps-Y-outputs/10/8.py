
def f1(n, s, m, dictionary):
    # Initialize variables
    correct_translations = 0
    incorrect_translations = 0
    
    # Iterate through each word in the sentence
    for word in s.split():
        # Check if the word is in the dictionary
        if word in dictionary:
            # If the word is in the dictionary, check if it is a correct translation
            if dictionary[word] == "correct":
                correct_translations += 1
            else:
                incorrect_translations += 1
        else:
            # If the word is not in the dictionary, it is an incorrect translation
            incorrect_translations += 1
    
    # Return the number of correct and incorrect translations
    return correct_translations, incorrect_translations

def f2(n, s, m, dictionary):
    # Initialize variables
    correct_translations = 0
    incorrect_translations = 0
    
    # Iterate through each word in the sentence
    for word in s.split():
        # Check if the word is in the dictionary
        if word in dictionary:
            # If the word is in the dictionary, check if it is a correct translation
            if dictionary[word] == "correct":
                correct_translations += 1
            else:
                incorrect_translations += 1
        else:
            # If the word is not in the dictionary, it is an incorrect translation
            incorrect_translations += 1
    
    # Return the number of correct and incorrect translations
    return correct_translations, incorrect_translations

if __name__ == '__main__':
    n = int(input())
    s = input()
    m = int(input())
    dictionary = {}
    for i in range(m):
        word, translation, correctness = input().split()
        dictionary[word] = translation
    
    correct_translations, incorrect_translations = f1(n, s, m, dictionary)
    print(correct_translations, "correct")
    print(incorrect_translations, "incorrect")

