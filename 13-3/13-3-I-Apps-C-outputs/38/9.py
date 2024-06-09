
def get_power(word):
    power = 0
    for i in range(len(word) - 3):
        subword = word[i:i+4]
        if subword == subword[::-1]:
            power += 1
    return power

