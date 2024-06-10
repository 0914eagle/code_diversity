
def nimionese(word):
    # Replace the first letter with the nearest hard consonant
    if word[0] in ['b', 'c', 'd', 'g', 'k', 'n', 'p', 't']:
        word = word.replace(word[0], 'b')
    # Replace "each" with "Dach"
    if word == "each":
        word = "Dach"
    # Replace hard consonants in subsequent syllables with the same consonant as the first letter
    if word[0] in ['b', 'c', 'd', 'g', 'k', 'n', 'p', 't']:
        word = word.replace(word[0], word[0].upper())
    # Add "ah", "oh", or "uh" at the end of the word
    if word[-1] in ['b', 'c', 'd', 'g', 'k', 'n', 'p', 't']:
        word = word + "ah"
    return word

def nimionese_sentence(sentence):
    # Split the sentence into words
    words = sentence.split()
    # Convert each word to nimionese
    nimionese_words = [nimionese(word) for word in words]
    # Join the nimionese words into a sentence
    nimionese_sentence = " ".join(nimionese_words)
    return nimionese_sentence

if __name__ == '__main__':
    sentence = input()
    print(nimionese_sentence(sentence))

