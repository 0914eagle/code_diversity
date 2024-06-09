
def f1(word):
    # find the maximum subword of the form $ww^Rww^R$
    subword = ""
    for i in range(len(word)):
        if word[i] == word[len(word)-i-1]:
            subword = word[i:len(word)-i]
    # return the length of the subword
    return len(subword)

def f2(word):
    # find the power of the word
    power = f1(word)
    # return the power of the word
    return power

if __name__ == '__main__':
    word = input()
    print(f2(word))

