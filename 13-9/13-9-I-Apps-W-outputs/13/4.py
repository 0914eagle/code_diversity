
def get_compressed_word(sentence):
    n = len(sentence)
    if n == 1:
        return sentence[0]
    
    compressed_word = sentence[0]
    for i in range(1, n):
        word = sentence[i]
        prefix = ""
        for j in range(len(word)):
            if word[j] == compressed_word[-1]:
                prefix += word[j]
            else:
                break
        compressed_word += word[len(prefix):]
    return compressed_word

def main():
    n = int(input())
    sentence = input().split()
    print(get_compressed_word(sentence))

if __name__ == '__main__':
    main()

