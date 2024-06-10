
def get_typo_indexes(word):
    # Find the indexes of the typos in the word
    typo_indexes = []
    for i in range(len(word) - 2):
        if word[i] == word[i + 1] == word[i + 2]:
            typo_indexes.append(i)
    for i in range(len(word) - 3):
        if word[i] == word[i + 1] == word[i + 2] == word[i + 3]:
            typo_indexes.append(i)
    return typo_indexes

def delete_min_num_letters(word):
    # Get the indexes of the typos in the word
    typo_indexes = get_typo_indexes(word)
    
    # If there are no typos, return the original word
    if not typo_indexes:
        return word
    
    # Find the minimum number of letters that need to be deleted to correct the typos
    min_num_letters = float('inf')
    for i in range(len(typo_indexes)):
        num_letters = len(word) - (typo_indexes[i] + 1)
        if num_letters < min_num_letters:
            min_num_letters = num_letters
    
    # Delete the minimum number of letters from the word to correct the typos
    return word[:min_num_letters]

def main():
    word = input()
    print(delete_min_num_letters(word))

if __name__ == '__main__':
    main()

