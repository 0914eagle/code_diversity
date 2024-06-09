
def is_correct_translation(dutch_sentence, english_translation):
    # Split the Dutch sentence into words
    dutch_words = dutch_sentence.split()
    # Split the English translation into words
    english_words = english_translation.split()
    # Check if the number of words in the Dutch sentence and English translation match
    if len(dutch_words) != len(english_words):
        return False
    # Check if each word in the Dutch sentence has a corresponding correct translation in the English translation
    for i in range(len(dutch_words)):
        if dutch_words[i] not in english_words[i]:
            return False
    return True

def get_translations(dutch_sentence, dictionary):
    # Initialize a list to store the translations
    translations = []
    # Iterate over the dictionary
    for dutch_word, english_word, correct in dictionary:
        # Check if the Dutch word is in the sentence
        if dutch_word in dutch_sentence:
            # Add the English word to the list of translations
            translations.append(english_word)
    # Return the list of translations
    return translations

def main():
    # Read the number of words in the Dutch sentence and the sentence
    n = int(input())
    dutch_sentence = input()
    # Read the number of words in the dictionary and the dictionary
    m = int(input())
    dictionary = []
    for i in range(m):
        dutch_word, english_word, correct = input().split()
        dictionary.append((dutch_word, english_word, correct))
    # Get the translations of the Dutch sentence
    translations = get_translations(dutch_sentence, dictionary)
    # Initialize the number of correct and incorrect translations
    num_correct = 0
    num_incorrect = 0
    # Iterate over the translations
    for translation in translations:
        # Check if the translation is correct
        if is_correct_translation(dutch_sentence, translation):
            num_correct += 1
        else:
            num_incorrect += 1
    # Print the number of correct and incorrect translations
    print(num_correct, "correct")
    print(num_incorrect, "incorrect")

if __name__ == "__main__":
    main()

