
def nimionese(word):
    # Replace first letter with nearest hard consonant
    if word[0] in "bcdfghjklmnpqrstvwxz":
        word = "b" + word[1:]
    elif word[0] in "yz":
        word = "z" + word[1:]
    
    # Replace "each" with "Dach"
    if word == "each":
        word = "Dach"
    
    # Replace hard consonants in subsequent syllables
    word = word.replace("b", "b")
    word = word.replace("c", "c")
    word = word.replace("d", "d")
    word = word.replace("g", "g")
    word = word.replace("k", "k")
    word = word.replace("n", "n")
    word = word.replace("p", "p")
    word = word.replace("t", "t")
    
    # Replace "hip-po" with "gip-go"
    if "hip-po" in word:
        word = word.replace("hip-po", "gip-go")
    
    # Add nearest vowel at the end of the word
    if word[-1] in "bcdfghjklmnpqrstvwxz":
        word = word + "ah"
    elif word[-1] in "yz":
        word = word + "uh"
    
    return word

def nimionese_sentence(sentence):
    words = sentence.split()
    nimionese_words = [nimionese(word) for word in words]
    return " ".join(nimionese_words)

if __name__ == '__main__':
    sentence = input()
    print(nimionese_sentence(sentence))

