
def find_typos(word):
    # Initialize a variable to keep track of the minimum number of letters to delete
    min_deletions = len(word)
    # Initialize a variable to keep track of the word with the minimum number of deletions
    optimal_word = word
    
    # Iterate over all possible positions to delete letters
    for i in range(len(word)):
        # Iterate over all possible lengths to delete letters
        for j in range(1, len(word) - i + 1):
            # Check if the current position and length form a typo
            if word[i:i+j] * 2 == word[i:i+j+j]:
                # If it is a typo, delete the letters and check if the word is still valid
                corrected_word = word[:i] + word[i+j:]
                if corrected_word.isalpha():
                    # If the word is valid, check if the number of deletions is less than the current minimum
                    if len(corrected_word) < min_deletions:
                        # If it is, update the minimum number of deletions and the optimal word
                        min_deletions = len(corrected_word)
                        optimal_word = corrected_word
    
    return optimal_word

def main():
    word = input("Enter a word: ")
    print(find_typos(word))

if __name__ == '__main__':
    main()

