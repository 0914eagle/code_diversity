
def merge_words(words):
    result = ""
    for word in words:
        if result:
            result = merge_word(result, word)
        else:
            result = word
    return result

def merge_word(word1, word2):
    for i in range(len(word2)):
        if word1.endswith(word2[:i]):
            return word1 + word2[i:]
    return word1 + word2

def main():
    n = int(input())
    words = input().split()
    print(merge_words(words))

if __name__ == '__main__':
    main()

