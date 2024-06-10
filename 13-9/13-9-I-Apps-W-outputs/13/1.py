
def get_compressed_word(sentence):
    n = len(sentence)
    if n == 1:
        return sentence[0]
    else:
        first_word = sentence[0]
        second_word = sentence[1]
        longest_prefix = ""
        for i in range(len(second_word)):
            if second_word[:i+1] == first_word[-i-1:]:
                longest_prefix = second_word[:i+1]
        return first_word[:-len(longest_prefix)] + second_word[len(longest_prefix):]

def main():
    n = int(input())
    sentence = input().split()
    compressed_word = get_compressed_word(sentence)
    print(compressed_word)

if __name__ == '__main__':
    main()

