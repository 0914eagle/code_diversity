
def get_cyclic_shift_words(word):
    words = set()
    words.add(word)
    for i in range(len(word)):
        words.add(word[i:] + word[:i])
    return len(words)

def main():
    word = input()
    print(get_cyclic_shift_words(word))

if __name__ == '__main__':
    main()

