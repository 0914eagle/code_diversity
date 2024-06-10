
def nimionese(word):
    # Replace the first letter with the nearest hard consonant
    word = word.replace(word[0], "bcdgknpt"["abcdefghijklmnopqrstuvwxyz".index(word[0])])
    
    # Replace "each" with "Dach"
    word = word.replace("each", "Dach")
    
    # Replace hard consonants in subsequent syllables with the same consonant as the first letter
    word = word.replace(word[1], word[0])
    
    # Add "ah", "oh", or "uh" at the end of the word, rounding towards "A" in case of a tie
    word = word[:-1] + "ah"
    
    return word

def nimionese_sentence(sentence):
    # Split the sentence into words
    words = sentence.split()
    
    # Translate each word to nimionese
    nimionese_words = [nimionese(word) for word in words]
    
    # Join the translated words into a sentence
    nimionese_sentence = " ".join(nimionese_words)
    
    return nimionese_sentence

if __name__ == '__main__':
    sentence = input()
    print(nimionese_sentence(sentence))

