
def delete_typos(word):
    # Initialize a variable to store the minimum number of letters to delete
    min_deletions = len(word)
    # Initialize a variable to store the corrected word
    corrected_word = word

    # Loop through the word and check for typos
    for i in range(len(word) - 2):
        # Check if the current letter is identical to the next two letters
        if word[i] == word[i + 1] == word[i + 2]:
            # Delete the current letter and the next two letters
            corrected_word = corrected_word[:i] + corrected_word[i + 3:]
            # Update the minimum number of letters to delete
            min_deletions = min(min_deletions, len(word) - len(corrected_word))

    # Loop through the word and check for typos
    for i in range(len(word) - 4):
        # Check if the current letter is identical to the next letter and the letter after that
        if word[i] == word[i + 1] == word[i + 2]:
            # Delete the current letter and the next two letters
            corrected_word = corrected_word[:i] + corrected_word[i + 3:]
            # Update the minimum number of letters to delete
            min_deletions = min(min_deletions, len(word) - len(corrected_word))

    return corrected_word

def main():
    word = input("Enter a word: ")
    corrected_word = delete_typos(word)
    print(f"Corrected word: {corrected_word}")

if __name__ == '__main__':
    main()

