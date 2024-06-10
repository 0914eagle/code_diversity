
def input_words(n):
    return input().split()

def merge_words(words):
    merged_word = ""
    for i in range(len(words)):
        if i == 0:
            merged_word = words[i]
        else:
            merged_word = merge_two_words(merged_word, words[i])
    return merged_word

def merge_two_words(word1, word2):
    i = 0
    while i < len(word2) and word2[i] == word1[-1]:
        i += 1
    return word1 + word2[i:]

def main():
    n = int(input())
    words = input_words(n)
    print(merge_words(words))

if __name__ == '__main__':
    main()

