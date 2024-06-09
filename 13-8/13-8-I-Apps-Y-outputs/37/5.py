
def decode_sentence(coded_sentence):
    vowels = ['a', 'e', 'i', 'o', 'u']
    decoded_sentence = ''
    for word in coded_sentence.split():
        decoded_word = ''
        for char in word:
            if char in vowels:
                decoded_word += 'p' + char + char
            else:
                decoded_word += char
        decoded_sentence += decoded_word + ' '
    return decoded_sentence.strip()

