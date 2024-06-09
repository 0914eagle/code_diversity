
def get_optimal_essay(essay, synonyms):
    # Initialize variables to keep track of the minimum number of Rs and length
    min_rs = float('inf')
    min_length = float('inf')
    
    # Loop through all possible synonyms
    for synonym in synonyms:
        # Replace the word with its synonym
        new_essay = essay.replace(synonym[0], synonym[1])
        
        # Calculate the number of Rs in the new essay
        num_rs = new_essay.lower().count('r')
        
        # If the number of Rs is less than the minimum, update the minimum
        if num_rs < min_rs:
            min_rs = num_rs
            min_length = len(new_essay)
    
    # Return the minimum number of Rs and length
    return min_rs, min_length

