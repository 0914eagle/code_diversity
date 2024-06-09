
def is_verse_pattern_matched(text, verse_pattern):
    # Initialize a list to store the number of syllables in each line
    syllable_counts = []
    
    # Iterate over the lines of the text
    for line in text:
        # Initialize a variable to store the number of syllables in the current line
        syllable_count = 0
        
        # Iterate over the words in the current line
        for word in line.split():
            # Check if the word contains a vowel
            if any(char in "aeiouy" for char in word):
                # If the word contains a vowel, increment the syllable count by 1
                syllable_count += 1
        
        # Add the syllable count for the current line to the list
        syllable_counts.append(syllable_count)
    
    # Check if the syllable counts match the verse pattern
    return syllable_counts == verse_pattern

def main():
    # Read the number of lines in the text and the verse pattern from stdin
    n = int(input())
    verse_pattern = list(map(int, input().split()))
    
    # Read the text from stdin
    text = [input() for _ in range(n)]
    
    # Check if the text matches the verse pattern
    if is_verse_pattern_matched(text, verse_pattern):
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()

