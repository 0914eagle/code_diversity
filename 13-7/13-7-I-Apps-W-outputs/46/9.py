
def get_optimal_essay(essay, synonyms):
    # Initialize variables
    min_r_count = float('inf')
    min_length = float('inf')
    optimal_essay = ''

    # Iterate through all possible synonyms
    for synonym in synonyms:
        # Replace word with its synonym
        new_essay = essay.replace(synonym[0], synonym[1])

        # Check if the number of Rs in the new essay is less than the minimum
        r_count = new_essay.lower().count('r')
        if r_count < min_r_count:
            min_r_count = r_count
            min_length = len(new_essay)
            optimal_essay = new_essay

    # Return the optimal essay
    return min_r_count, min_length

