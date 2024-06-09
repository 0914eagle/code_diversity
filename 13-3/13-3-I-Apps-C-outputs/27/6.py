
def is_verse_pattern_matched(text, verse_pattern):
    # Initialize variables
    syllables_count = 0
    words = text.split()
    
    # Iterate over the words and count the syllables
    for word in words:
        if any(letter in "aeiouy" for letter in word):
            syllables_count += 1
    
    # Check if the syllables count matches the verse pattern
    return syllables_count == verse_pattern

