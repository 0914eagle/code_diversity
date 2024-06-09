
def get_power(word):
    power = 0
    for i in range(len(word) - 1):
        if word[i] == word[i + 1]:
            power += 1
    return power

