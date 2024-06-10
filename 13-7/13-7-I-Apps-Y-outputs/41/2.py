
def nimionese(word):
    # Replace first letter with the nearest hard consonant
    if word[0] in "bcdfghjklmnpqrstvwxyz":
        word = "b" + word[1:]
    elif word[0] in "BCDFGHJKLMNPQRSTVWXYZ":
        word = "B" + word[1:]
    
    # Replace "each" with "Dach"
    if word == "each":
        word = "Dach"
    
    # Replace hard consonants in subsequent syllables with the same consonant as the first letter
    for i in range(1, len(word)):
        if word[i] in "bcdfghjklmnpqrstvwxyz":
            word = word[:i] + "b" + word[i+1:]
        elif word[i] in "BCDFGHJKLMNPQRSTVWXYZ":
            word = word[:i] + "B" + word[i+1:]
    
    # Add "ah", "oh", or "uh" to the end of the word, whichever is nearest, rounding toward "A" in the case of a tie
    if word[-1] in "bcdfghjklmnpqrstvwxyz":
        word += "ah"
    elif word[-1] in "BCDFGHJKLMNPQRSTVWXYZ":
        word += "Ah"
    
    return word

def nimionese_sentence(sentence):
    words = sentence.split()
    nimionese_words = [nimionese(word) for word in words]
    return " ".join(nimionese_words)

def main():
    sentence = input()
    print(nimionese_sentence(sentence))

if __name__ == '__main__':
    main()

