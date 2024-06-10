
def get_compressed_word(sentence):
    n = len(sentence)
    if n == 1:
        return sentence[0]
    else:
        first_word = sentence[0]
        second_word = sentence[1]
        compressed_word = first_word + second_word
        for i in range(2, n):
            word = sentence[i]
            longest_prefix = ""
            for j in range(len(word)):
                if word[j:] == compressed_word[:j]:
                    longest_prefix = word[:j]
                    break
            compressed_word = compressed_word[len(longest_prefix):] + word[len(longest_prefix):]
        return compressed_word

def main():
    sentence = input().split()
    print(get_compressed_word(sentence))

if __name__ == '__main__':
    main()

