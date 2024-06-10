
def nimionese(word):
    # Replace first letter with nearest hard consonant
    if word[0] in ["b", "c", "d", "g", "k", "n", "p", "t"]:
        word = "hard" + word[1:]
    # Replace "each" with "Dach"
    if word == "each":
        word = "Dach"
    # Replace hard consonants in subsequent syllables with same consonant as first letter
    if word[0] in ["b", "c", "d", "g", "k", "n", "p", "t"]:
        word = word.replace(word[0], "hard")
    # Add "ah", "oh", or "uh" to end of word
    if word[-1] in ["b", "c", "d", "g", "k", "n", "p", "t"]:
        if word[-1] == "b":
            word = word[:-1] + "ah"
        elif word[-1] == "c":
            word = word[:-1] + "oh"
        else:
            word = word[:-1] + "uh"
    return word

def nimionese_sentence(sentence):
    words = sentence.split()
    nimionese_words = [nimionese(word) for word in words]
    return " ".join(nimionese_words)

if __name__ == '__main__':
    sentence = input()
    print(nimionese_sentence(sentence))

