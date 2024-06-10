
def get_input():
    n = int(input())
    words = input().split()
    return n, words

def merge_words(words):
    merged_word = ""
    for i in range(len(words)):
        if i == 0:
            merged_word = words[i]
        else:
            merged_word = merge_two_words(merged_word, words[i])
    return merged_word

def merge_two_words(word1, word2):
    for i in range(len(word1)):
        if word1[:i] == word2[-i:]:
            return word1 + word2[i:]
    return word1 + word2

def main():
    n, words = get_input()
    merged_word = merge_words(words)
    print(merged_word)

if __name__ == '__main__':
    main()

