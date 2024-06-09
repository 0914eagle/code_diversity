
def get_optimal_essay(essay, synonyms):
    # Initialize the minimum number of letters 'R' and minimum length as infinity
    min_r_count, min_length = float('inf'), float('inf')
    # Loop through all possible synonyms
    for word1, word2 in synonyms:
        # Replace the word with its synonym in the essay
        essay = essay.replace(word1, word2)
        # Get the number of letters 'R' in the essay
        r_count = essay.lower().count('r')
        # Get the length of the essay
        length = len(essay)
        # If the number of letters 'R' is less than the minimum,
        # or if the number of letters 'R' is the same but the length is less,
        # update the minimum number of letters 'R' and minimum length
        if r_count < min_r_count or (r_count == min_r_count and length < min_length):
            min_r_count, min_length = r_count, length
    # Return the minimum number of letters 'R' and minimum length
    return min_r_count, min_length

