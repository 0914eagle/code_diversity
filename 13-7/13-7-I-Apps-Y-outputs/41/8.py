
def convert_to_nimionese(word):
    # Replace first letter with the nearest hard consonant
    word = word.replace(word[0], get_nearest_hard_consonant(word[0]))
    
    # Replace "each" with "dach"
    word = word.replace("each", "dach")
    
    # Replace hard consonants in subsequent syllables with the same consonant as the first letter
    word = word.replace(word[1:], get_nearest_hard_consonant(word[0]))
    
    # Add "ah", "oh", or "uh" at the end of the word, rounding toward "A" in case of a tie
    word = word + get_nearest_ending(word[-1])
    
    return word

def get_nearest_hard_consonant(letter):
    hard_consonants = ["b", "c", "d", "g", "k", "n", "p", "t"]
    index = hard_consonants.index(letter)
    return hard_consonants[index]

def get_nearest_ending(letter):
    endings = ["ah", "oh", "uh"]
    index = endings.index(letter)
    return endings[index]

def main():
    sentence = input()
    nimionese_sentence = ""
    
    for word in sentence.split():
        nimionese_word = convert_to_nimionese(word)
        nimionese_sentence += nimionese_word + " "
    
    print(nimionese_sentence.strip())

if __name__ == '__main__':
    main()

