
def get_compressed_word(sentence):
    words = sentence.split()
    compressed_word = words[0]
    for word in words[1:]:
        compressed_word = merge_words(compressed_word, word)
    return compressed_word

def merge_words(word1, word2):
    i = 0
    while i < len(word2) and word2[i] == word1[-1]:
        i += 1
    return word1 + word2[i:]

if __name__ == '__main__':
    sentence = input()
    print(get_compressed_word(sentence))

