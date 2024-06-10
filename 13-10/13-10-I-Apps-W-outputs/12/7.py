
def correct_typo(word):
    # Delete all instances of three identical letters in a row
    word = word.replace(word[0] * 3, word[0])
    
    # Delete all instances of four identical letters in a row
    word = word.replace(word[0] * 4, word[0])
    
    # Delete all instances of five identical letters in a row
    word = word.replace(word[0] * 5, word[0])
    
    return word

def delete_min_letters(word):
    # Initialize variables
    min_deletions = len(word)
    corrected_word = word
    
    # Iterate through all possible starting indices
    for i in range(len(word)):
        # Iterate through all possible ending indices
        for j in range(i + 1, len(word) + 1):
            # Extract the substring from i to j
            substring = word[i:j]
            
            # Check if the substring contains a typo
            if len(substring) > 1 and substring[0] == substring[-1]:
                # Delete the substring and check if the number of deletions is minimal
                corrected_substring = word[:i] + word[j:]
                if len(corrected_substring) < min_deletions:
                    min_deletions = len(corrected_substring)
                    corrected_word = corrected_substring
    
    return corrected_word

if __name__ == '__main__':
    word = input()
    corrected_word = delete_min_letters(word)
    print(corrected_word)

