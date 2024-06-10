
def correct_typos(word):
    # Initialize a variable to store the corrected word
    corrected_word = ""
    # Initialize a variable to store the number of consecutive identical letters
    consecutive_letters = 1
    # Iterate through the word
    for i in range(len(word) - 1):
        # If the current letter is the same as the next letter, increment the consecutive_letters counter
        if word[i] == word[i + 1]:
            consecutive_letters += 1
        # If the current letter is not the same as the next letter or we have reached the end of the word, check if we have found a typo
        else:
            # If we have found a typo, delete the minimum number of letters to correct it
            if consecutive_letters >= 3:
                # If we are deleting letters from the beginning of the word, delete the entire group of consecutive letters
                if i < len(word) - consecutive_letters:
                    word = word[consecutive_letters:]
                # If we are deleting letters from the end of the word, delete the entire group of consecutive letters
                else:
                    word = word[:-consecutive_letters]
            # Reset the consecutive_letters counter
            consecutive_letters = 1
    # If we have reached the end of the word and there are still consecutive identical letters, delete the minimum number of letters to correct it
    if consecutive_letters >= 3:
        # If we are deleting letters from the beginning of the word, delete the entire group of consecutive letters
        if len(word) - consecutive_letters > 0:
            word = word[consecutive_letters:]
        # If we are deleting letters from the end of the word, delete the entire group of consecutive letters
        else:
            word = word[:-consecutive_letters]
    # Return the corrected word
    return word

def main():
    # Read a single line of input containing the word
    word = input()
    # Correct the typos in the word
    corrected_word = correct_typos(word)
    # Print the corrected word
    print(corrected_word)

if __name__ == '__main__':
    main()

