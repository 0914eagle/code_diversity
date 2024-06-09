
def decode_sentence(sentence):
    vowels = ['a', 'e', 'i', 'o', 'u']
    decoded_sentence = ''
    for char in sentence:
        if char in vowels:
            decoded_sentence += char + 'p' + char
        else:
            decoded_sentence += char
    return decoded_sentence

