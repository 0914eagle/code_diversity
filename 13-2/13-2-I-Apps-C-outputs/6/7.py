
def solve(message):
    # Split the message into individual words
    words = message.split()
    
    # Create a dictionary of words and their vowel counts
    word_vowels = {}
    for word in words:
        vowel_count = 0
        for letter in word:
            if letter in "AEIOU":
                vowel_count += 1
        word_vowels[word] = vowel_count
    
    # Sort the words by vowel count in descending order
    sorted_words = sorted(word_vowels.items(), key=lambda x: x[1], reverse=True)
    
    # Reconstruct the original sentence
    sentence = []
    for word, vowel_count in sorted_words:
        sentence.append(word)
    
    return " ".join(sentence)

