
def convert_to_nimionese(word):
    # Replace first letter with nearest hard consonant
    if word[0] in ["b", "c", "d", "g", "k", "n", "p", "t"]:
        word = "hard" + word[1:]
    # Replace "each" with "Dach"
    if word == "each":
        word = "Dach"
    # Replace hard consonants in subsequent syllables with same consonant as first letter
    if word[0] in ["b", "c", "d", "g", "k", "n", "p", "t"]:
        word = word.replace(word[0], "hard")
    # Add nearest vowel to end of word
    if word[-1] in ["b", "c", "d", "g", "k", "n", "p", "t"]:
        if word[-1] == "b":
            word += "ah"
        elif word[-1] == "c":
            word += "oh"
        elif word[-1] == "d":
            word += "ah"
        elif word[-1] == "g":
            word += "oh"
        elif word[-1] == "k":
            word += "ah"
        elif word[-1] == "n":
            word += "ah"
        elif word[-1] == "p":
            word += "ah"
        elif word[-1] == "t":
            word += "ah"
    return word

def nimionese_translator(sentence):
    words = sentence.split()
    nimionese_words = [convert_to_nimionese(word) for word in words]
    return " ".join(nimionese_words)

if __name__ == '__main__':
    sentence = input()
    print(nimionese_translator(sentence))

