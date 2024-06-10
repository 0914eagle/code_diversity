
def correct_typos(word):
    # Initialize variables
    corrected_word = word
    num_deletions = 0
    
    # Loop through the word and check for typos
    for i in range(len(word) - 1):
        # Check for triplets of identical letters
        if word[i] == word[i + 1] == word[i + 2]:
            corrected_word = corrected_word[:i] + corrected_word[i + 1:]
            num_deletions += 1
        # Check for pairs of identical letters followed by pairs of identical letters
        elif word[i] == word[i + 1] and word[i + 1] == word[i + 2]:
            corrected_word = corrected_word[:i] + corrected_word[i + 2:]
            num_deletions += 2
    
    return corrected_word, num_deletions

def main():
    word = input("Enter a word: ")
    corrected_word, num_deletions = correct_typos(word)
    print(f"The corrected word is: {corrected_word}")
    print(f"The number of deletions needed is: {num_deletions}")

if __name__ == '__main__':
    main()

