
def get_optimal_essay(essay, synonyms):
    # Initialize variables to keep track of the minimum number of Rs and the minimum length
    min_rs = float('inf')
    min_length = float('inf')
    
    # Iterate through all possible combinations of synonyms
    for synonym_combination in itertools.combinations(synonyms, len(essay)):
        # Create a copy of the essay with the current combination of synonyms
        essay_copy = essay[:]
        for i, synonym in enumerate(synonym_combination):
            essay_copy[i] = synonym
        # Count the number of Rs in the current essay
        num_rs = sum(1 for word in essay_copy if 'r' in word.lower())
        # Count the length of the current essay
        length = sum(len(word) for word in essay_copy)
        # If the current essay is better than the previous best, update the variables
        if num_rs < min_rs or (num_rs == min_rs and length < min_length):
            min_rs = num_rs
            min_length = length
    
    # Return the minimum number of Rs and the minimum length of the optimal essay
    return min_rs, min_length

