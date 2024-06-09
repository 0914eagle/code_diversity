
def f1(N, words):
    # Initialize the dictionary with the most common words
    dictionary = {word: i for i, word in enumerate(words, start=1)}
    return dictionary

def f2(dictionary, word):
    # Initialize the current word and the number of key presses
    current_word = word
    key_presses = 0

    # Loop through the characters in the word
    for char in word:
        # If the character is not in the dictionary, break the loop
        if char not in dictionary:
            break
        # Otherwise, increment the key presses and update the current word
        key_presses += 1
        current_word = dictionary[char]

    # If the word is fully typed, return the key presses
    if current_word == word:
        return key_presses

    # If the word is not fully typed, find the shortest word in the dictionary
    # that is a prefix of the current word
    shortest_word = ""
    for i in range(len(word)):
        prefix = word[:i+1]
        if prefix in dictionary:
            shortest_word = prefix
            break

    # If no shortest word is found, return -1
    if not shortest_word:
        return -1

    # Otherwise, return the key presses for the shortest word plus the key presses
    # for the remaining characters
    return key_presses + f2(dictionary, word[len(shortest_word):])

if __name__ == '__main__':
    N = int(input())
    words = [input() for _ in range(N)]
    dictionary = f1(N, words)
    Q = int(input())
    for _ in range(Q):
        word = input()
        print(f2(dictionary, word))

