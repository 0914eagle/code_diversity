
def correct_typos(word):
    # Initialize variables
    corrected_word = word
    typos_deleted = 0

    # Check for triple letters
    while corrected_word.find('ccc') != -1:
        corrected_word = corrected_word.replace('ccc', 'c')
        typos_deleted += 1

    # Check for double letters followed by double letters
    while corrected_word.find('dd') != -1:
        corrected_word = corrected_word.replace('dd', '')
        typos_deleted += 1

    return corrected_word, typos_deleted

def main():
    word = input("Enter a word: ")
    corrected_word, typos_deleted = correct_typos(word)
    print(f"Corrected word: {corrected_word}")
    print(f"Typos deleted: {typos_deleted}")

if __name__ == '__main__':
    main()

