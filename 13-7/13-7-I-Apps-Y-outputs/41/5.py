
def translate_to_nimionese(word):
    # Replace the first letter of the word with the nearest hard consonant
    word = word.replace(word[0], get_nearest_hard_consonant(word[0]))
    
    # Replace "each" with "Dach"
    word = word.replace("each", "Dach")
    
    # Replace hard consonants in subsequent syllables with the same consonant as the first letter
    word = word.replace(word[1:], word[0] * (len(word) - 1))
    
    # Add an "ah", "oh", or "uh" at the end of the word, whichever is nearest to "A"
    word = word + get_nearest_vowel(word[-1])
    
    return word

def get_nearest_hard_consonant(letter):
    hard_consonants = ["b", "c", "d", "g", "k", "n", "p", "t"]
    index = hard_consonants.index(letter)
    return hard_consonants[(index + 1) % len(hard_consonants)]

def get_nearest_vowel(letter):
    vowels = ["a", "e", "i", "o", "u"]
    index = vowels.index(letter)
    return vowels[(index + 1) % len(vowels)]

def main():
    sentence = input()
    translated_sentence = ""
    
    for word in sentence.split():
        translated_word = translate_to_nimionese(word)
        translated_sentence += translated_word + " "
    
    print(translated_sentence.strip())

if __name__ == '__main__':
    main()

