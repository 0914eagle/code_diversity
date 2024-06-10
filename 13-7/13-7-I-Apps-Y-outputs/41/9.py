
def nimionese(sentence):
    # Split the sentence into a list of words
    words = sentence.split()
    
    # Create a list to store the nimionese words
    nimionese_words = []
    
    # Iterate through the words and convert them to nimionese
    for word in words:
        # Check if the word is "each"
        if word == "each":
            nimionese_words.append("Dach")
        # Check if the word starts with a hard consonant
        elif word[0] in ["b", "c", "d", "g", "k", "n", "p", "t"]:
            # Replace the first letter with the nearest hard consonant to "A"
            nimionese_words.append(word[0].replace(word[0], "b") + word[1:])
        # Check if the word ends with a hard consonant
        elif word[-1] in ["b", "c", "d", "g", "k", "n", "p", "t"]:
            # Add an "ah", "oh", or "uh" at the end of the word, rounding toward "A" in the case of a tie
            nimionese_words.append(word[:-1] + "ah")
        # Check if the word contains a hyphen
        elif "-" in word:
            # Split the word into syllables and convert each syllable to nimionese
            syllables = word.split("-")
            nimionese_syllables = []
            for syllable in syllables:
                # Check if the syllable is "hip-po"
                if syllable == "hip-po":
                    nimionese_syllables.append("gip-go")
                # Check if the syllable starts with a hard consonant
                elif syllable[0] in ["b", "c", "d", "g", "k", "n", "p", "t"]:
                    # Replace the first letter with the nearest hard consonant to "A"
                    nimionese_syllables.append(syllable[0].replace(syllable[0], "b") + syllable[1:])
                # Check if the syllable ends with a hard consonant
                elif syllable[-1] in ["b", "c", "d", "g", "k", "n", "p", "t"]:
                    # Add an "ah", "oh", or "uh" at the end of the syllable, rounding toward "A" in the case of a tie
                    nimionese_syllables.append(syllable[:-1] + "ah")
                # Otherwise, just add the syllable to the list
                else:
                    nimionese_syllables.append(syllable)
            # Join the nimionese syllables back together to form the nimionese word
            nimionese_words.append("-".join(nimionese_syllables))
        # Otherwise, just add the word to the list
        else:
            nimionese_words.append(word)
    
    # Join the nimionese words back together to form the nimionese sentence
    nimionese_sentence = " ".join(nimionese_words)
    
    return nimionese_sentence

def main():
    sentence = input("Enter a sentence: ")
    print(nimionese(sentence))

if __name__ == '__main__':
    main()

