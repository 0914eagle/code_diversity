
def check_typos(word):
    # Initialize a variable to store the corrected word
    corrected_word = ""

    # Iterate through the word
    for i in range(len(word)):
        # Check if the current letter is identical to the previous letter
        if i > 0 and word[i] == word[i-1]:
            # If it is, skip the current letter
            continue
        # Check if the current letter is identical to the next letter
        if i < len(word) - 1 and word[i] == word[i+1]:
            # If it is, skip the current letter
            continue
        # If the current letter is not identical to the previous or next letter, add it to the corrected word
        corrected_word += word[i]

    return corrected_word

def main():
    # Read a line of input from stdin and convert it to an integer
    word = input().strip()

    # Call the check_typos function and store the returned value in a variable
    corrected_word = check_typos(word)

    # Print the corrected word to stdout
    print(corrected_word)

if __name__ == '__main__':
    main()

