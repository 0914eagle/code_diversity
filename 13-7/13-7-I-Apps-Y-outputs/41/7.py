
def translate_to_nimionese(word):
    # Replace the first letter with the nearest hard consonant
    word = word.replace(word[0], get_nearest_hard_consonant(word[0]))
    
    # Replace "each" with "Dach"
    word = word.replace("each", "Dach")
    
    # Replace hard consonants in subsequent syllables with the same consonant as the first letter
    word = word.replace(word[1], get_nearest_hard_consonant(word[1]))
    
    # Add "ah", "oh", or "uh" to the end of the word, whichever is nearest to "A"
    word = word + get_ending_sound(word[-1])
    
    return word

def get_nearest_hard_consonant(letter):
    # Create a dictionary of hard consonants and their nearest neighbors
    hard_consonants = {
        "b": "a",
        "c": "b",
        "d": "c",
        "g": "d",
        "k": "g",
        "n": "k",
        "p": "n",
        "t": "p"
    }
    
    # Return the nearest hard consonant for the given letter
    return hard_consonants[letter]

def get_ending_sound(letter):
    # Create a dictionary of ending sounds and their nearest neighbors
    ending_sounds = {
        "a": "ah",
        "h": "uh",
        "k": "oh"
    }
    
    # Return the nearest ending sound for the given letter
    return ending_sounds[letter]

def main():
    sentence = input("Enter a sentence: ")
    nimionese_sentence = ""
    
    # Split the sentence into words and translate each word to nimionese
    for word in sentence.split():
        nimionese_word = translate_to_nimionese(word)
        nimionese_sentence += nimionese_word + " "
    
    print(nimionese_sentence.strip())

if __name__ == '__main__':
    main()

