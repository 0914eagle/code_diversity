
def f1(word):
    # find the maximum subword of the form $ww^Rww^R$
    subword = ""
    for i in range(len(word)):
        if word[i] == word[len(word)-i-1]:
            subword = word[i:len(word)-i]
    # calculate the power of the subword
    power = len(subword)
    # return the power
    return power

def f2(word):
    # check if the word is a palindrome
    if word == word[::-1]:
        return 0
    # find the maximum subword of the form $ww^Rww^R$
    subword = ""
    for i in range(len(word)):
        if word[i] == word[len(word)-i-1]:
            subword = word[i:len(word)-i]
    # calculate the power of the subword
    power = len(subword)
    # return the power
    return power

if __name__ == '__main__':
    word = input()
    power = f1(word)
    print(power)

