
def f1(word):
    # find the maximum subword of the form $ww^Rww^R$
    subword = ""
    for i in range(len(word)):
        for j in range(i+1, len(word)):
            if word[i:j] == word[j-1:i-1:-1]:
                subword = word[i:j]
                break
        if subword:
            break
    # calculate the power of the word
    power = len(subword) * 4
    return power

def f2(word):
    # find the maximum subword of the form $ww^Rww^R$
    subword = ""
    for i in range(len(word)):
        for j in range(i+1, len(word)):
            if word[i:j] == word[j-1:i-1:-1]:
                subword = word[i:j]
                break
        if subword:
            break
    # calculate the power of the word
    power = len(subword) * 4
    return power

if __name__ == '__main__':
    word = input()
    power = f1(word)
    print(power)

