
def get_optimal_essay(essay, synonyms):
    # Initialize variables to keep track of the minimum number of Rs and minimum length
    min_rs = float('inf')
    min_length = float('inf')
    
    # Loop through each synonym pair in the dictionary
    for x, y in synonyms:
        # If the essay contains the word x, replace it with y
        if x in essay:
            essay = essay.replace(x, y)
    
    # Count the number of Rs in the essay
    rs_count = essay.lower().count('r')
    
    # If the number of Rs is less than the current minimum, update the minimum
    if rs_count < min_rs:
        min_rs = rs_count
    
    # Calculate the length of the essay
    length = len(essay.split())
    
    # If the length is less than the current minimum, update the minimum
    if length < min_length:
        min_length = length
    
    # Return the minimum number of Rs and minimum length
    return min_rs, min_length

