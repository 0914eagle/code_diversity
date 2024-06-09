
def decode_sentence(coded_sentence):
    decoded_sentence = ""
    for char in coded_sentence:
        if char in "aeiou":
            decoded_sentence += "p" + char + char
        else:
            decoded_sentence += char
    return decoded_sentence

