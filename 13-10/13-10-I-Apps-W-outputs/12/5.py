
def check_typo(word):
    # Check if the word contains three identical letters together
    if len(set(word)) == len(word):
        return word
    
    # Check if the word contains a pair of identical letters followed by another pair of identical letters
    if len(word) > 3 and word[1] == word[0] and word[2] == word[1]:
        return word[0] + word[2:]
    
    # Check if the word contains a triplet of identical letters
    for i in range(len(word) - 2):
        if word[i] == word[i+1] == word[i+2]:
            return word[:i] + word[i+1:]
    
    # If no typos are found, return the original word
    return word

def correct_typos(word):
    # Delete letters from the beginning of the word until no typos are found
    while True:
        corrected_word = check_typo(word)
        if corrected_word == word:
            break
        word = corrected_word
    
    # Delete letters from the end of the word until no typos are found
    while True:
        corrected_word = check_typo(word[::-1])[::-1]
        if corrected_word == word:
            break
        word = corrected_word
    
    # If no typos are found in the middle of the word, return the original word
    return word

if __name__ == '__main__':
    word = input()
    print(correct_typos(word))

