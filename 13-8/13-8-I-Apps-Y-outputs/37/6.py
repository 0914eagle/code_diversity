
def decode_sentence(coded_sentence):
    decoded_sentence = ""
    vowels = ["a", "e", "i", "o", "u"]
    for char in coded_sentence:
        if char in vowels:
            decoded_sentence += char + "p" + char
        else:
            decoded_sentence += char
    return decoded_sentence

