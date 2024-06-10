
def get_compressed_word(sentence):
    n = len(sentence)
    if n == 1:
        return sentence[0]
    else:
        first_word = sentence[0]
        second_word = sentence[1]
        merged_word = merge_words(first_word, second_word)
        return merged_word + get_compressed_word(sentence[2:])

def merge_words(first_word, second_word):
    m = len(first_word)
    n = len(second_word)
    if m == 0 or n == 0:
        return first_word + second_word
    else:
        if first_word[m-1] == second_word[0]:
            return first_word[:m-1] + second_word
        else:
            return first_word + second_word

if __name__ == '__main__':
    sentence = input().split()
    compressed_word = get_compressed_word(sentence)
    print(compressed_word)

