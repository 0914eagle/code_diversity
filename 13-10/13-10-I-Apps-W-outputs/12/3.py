
def correct_typos(word):
    # Initialize a variable to store the corrected word
    corrected_word = ""

    # Iterate through the word
    for i in range(len(word)):
        # Check if the current character is identical to the previous character
        if i > 0 and word[i] == word[i-1]:
            # If it is, skip it
            continue
        # If it's not, add it to the corrected word
        corrected_word += word[i]

    # Return the corrected word
    return corrected_word

def delete_min_letters(word):
    # Initialize a variable to store the minimum number of letters to delete
    min_deletions = len(word)
    # Initialize a variable to store the corrected word with the minimum number of deletions
    corrected_word = word

    # Iterate through the length of the word
    for i in range(len(word)):
        # Get the substring of the word from 0 to i
        substr = word[:i+1]
        # Get the corrected substring by calling the correct_typos function
        corrected_substr = correct_typos(substr)
        # Get the number of letters to delete by subtracting the length of the corrected substring from the length of the original substring
        num_deletions = len(substr) - len(corrected_substr)
        # If the number of deletions is less than the minimum, update the minimum and the corrected word
        if num_deletions < min_deletions:
            min_deletions = num_deletions
            corrected_word = corrected_substr

    # Return the corrected word
    return corrected_word

if __name__ == '__main__':
    word = input("Enter a word: ")
    corrected_word = delete_min_letters(word)
    print(f"Corrected word: {corrected_word}")

