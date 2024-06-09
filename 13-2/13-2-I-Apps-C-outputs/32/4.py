
def solve(text, verse_pattern):
    # Initialize a list to store the number of syllables in each line
    syllable_count = [0] * len(text)

    # Iterate over the lines of the text
    for i, line in enumerate(text):
        # Split the line into words
        words = line.split()

        # Iterate over the words in the line
        for word in words:
            # Check if the word contains a vowel
            if any(char in "aeiou" for char in word):
                # If it does, increment the syllable count for the line
                syllable_count[i] += 1

    # Check if the syllable count for each line is equal to the corresponding element in the verse pattern
    return all(syllable_count[i] == verse_pattern[i] for i in range(len(text)))

