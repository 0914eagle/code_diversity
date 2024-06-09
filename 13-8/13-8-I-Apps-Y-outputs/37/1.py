
def decode_sentence(coded_sentence):
    decoded_sentence = ""
    for word in coded_sentence.split():
        decoded_word = ""
        for char in word:
            if char in "aeiou":
                decoded_word += "p" + char + char
            else:
                decoded_word += char
        decoded_sentence += decoded_word + " "
    return decoded_sentence.strip()

