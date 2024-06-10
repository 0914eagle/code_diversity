
def get_compressed_word(sentence):
    # Split the sentence into a list of words
    words = sentence.split()
    # Initialize the compressed word as the first word
    compressed_word = words[0]
    # Iterate through the remaining words
    for word in words[1:]:
        # Find the longest prefix of the current word that coincides with a suffix of the compressed word
        for i in range(len(word), 0, -1):
            if word[:i] == compressed_word[-i:]:
                # If a prefix is found, merge the words by removing the prefix and appending the remaining part of the current word
                compressed_word = compressed_word[:-i] + word[i:]
                break
        else:
            # If no prefix is found, simply append the current word to the compressed word
            compressed_word += " " + word
    return compressed_word.strip()

def main():
    sentence = input()
    print(get_compressed_word(sentence))

if __name__ == '__main__':
    main()

