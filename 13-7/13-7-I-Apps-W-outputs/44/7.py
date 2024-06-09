
def solve(word):
    vowels = set('aeiou')
    consonants = set('bcdfghjklmnpqrstvwxyz')

    # Check if the word has at least three consonants in a row
    if len(word) < 3:
        return word

    # Check if the word has at least two different letters in the block of consonants
    if len(set(word[1:4])) < 2:
        return word

    # Check if the block of consonants has all letters the same
    if len(set(word[1:4])) == 1:
        return word

    # Insert spaces into the word to divide it into two or more words
    words = []
    for i in range(len(word)):
        if word[i] in vowels or i == len(word) - 1:
            words.append(word[:i+1])
            word = word[i+1:]

    # Recursively call the function for each word
    return ' '.join([solve(word) for word in words])

