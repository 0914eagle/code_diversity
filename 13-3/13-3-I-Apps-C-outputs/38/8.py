
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
    # check if the word is a multiple of 4
    if len(word) % 4 == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    word = input()
    power = f1(word)
    if f2(word):
        print(power)
    else:
        print(0)

