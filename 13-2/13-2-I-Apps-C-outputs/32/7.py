
def solve(text, verse_pattern):
    # Initialize a list to store the number of syllables in each line
    syllable_count = [0] * len(text)

    # Iterate over the lines of text
    for i, line in enumerate(text):
        # Split the line into words
        words = line.split()

        # Iterate over the words in the line
        for word in words:
            # Check if the word contains a vowel
            if any(char in "aeiou" for char in word):
                # If it does, add the number of syllables in the word to the total for the line
                syllable_count[i] += 1 + word.count("-")

    # Check if the total number of syllables in each line matches the verse pattern
    return syllable_count == verse_pattern

