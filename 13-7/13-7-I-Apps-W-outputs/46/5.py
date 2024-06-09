
def get_optimal_essay(essay, synonyms):
    # Initialize variables to keep track of the minimum number of Rs and the minimum length of the essay
    min_rs = float('inf')
    min_length = float('inf')
    
    # Iterate through all possible synonyms for each word in the essay
    for word in essay.split():
        for synonym in synonyms:
            # If the synonym is a valid replacement for the word
            if word.lower() == synonym[0].lower():
                # Replace the word with the synonym and update the number of Rs and length of the essay
                essay = essay.replace(word, synonym[1])
                min_rs = min(min_rs, essay.count('r'))
                min_length = min(min_length, len(essay))
    
    # Return the minimum number of Rs and the minimum length of the essay
    return min_rs, min_length

