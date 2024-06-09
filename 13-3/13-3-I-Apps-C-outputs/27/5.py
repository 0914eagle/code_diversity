
def is_matching_verse_pattern(text, verse_pattern):
    # Initialize variables
    syllables_per_line = []
    vowels = ["a", "e", "i", "o", "u", "y"]
    
    # Iterate over the lines of the text
    for line in text:
        # Initialize variables for the current line
        syllables_in_line = 0
        words_in_line = line.split()
        
        # Iterate over the words in the current line
        for word in words_in_line:
            # Check if the word contains a vowel
            if any(vowel in word for vowel in vowels):
                # If it does, count the syllables in the word
                syllables_in_word = 1
                for char in word:
                    if char in vowels:
                        syllables_in_word += 1
                # Add the number of syllables in the word to the total for the line
                syllables_in_line += syllables_in_word
        
        # Add the number of syllables in the line to the list of syllables per line
        syllables_per_line.append(syllables_in_line)
    
    # Check if the number of syllables per line matches the verse pattern
    if syllables_per_line == verse_pattern:
        return "YES"
    else:
        return "NO"

