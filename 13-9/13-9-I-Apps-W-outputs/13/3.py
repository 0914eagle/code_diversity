
def get_compressed_word(words):
    compressed_word = ""
    for i in range(len(words)):
        if i == 0:
            compressed_word = words[i]
        else:
            compressed_word = merge_words(compressed_word, words[i])
    return compressed_word

def merge_words(word1, word2):
    longest_prefix = ""
    for i in range(len(word1), 0, -1):
        if word1[:i] == word2[-i:]:
            longest_prefix = word1[:i]
            break
    return word1[len(longest_prefix):] + word2[len(longest_prefix):]

if __name__ == '__main__':
    num_words = int(input())
    words = input().split()
    print(get_compressed_word(words))

