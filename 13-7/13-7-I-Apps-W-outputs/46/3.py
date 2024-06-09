
def get_optimal_essay(essay, synonym_dict):
    # Initialize variables to keep track of the minimum number of Rs and minimum length
    min_rs = float('inf')
    min_length = float('inf')
    
    # Loop through each word in the essay
    for word in essay:
        # Check if the word is in the synonym dictionary
        if word in synonym_dict:
            # If the word is in the dictionary, get its synonym
            synonym = synonym_dict[word]
            # Replace the word with its synonym in the essay
            essay = essay.replace(word, synonym)
    
    # Count the number of Rs in the essay
    num_rs = essay.lower().count('r')
    
    # If the number of Rs is less than the minimum, update the minimum
    if num_rs < min_rs:
        min_rs = num_rs
    
    # Get the length of the essay
    length = len(essay)
    
    # If the length is less than the minimum, update the minimum
    if length < min_length:
        min_length = length
    
    # Return the minimum number of Rs and minimum length
    return min_rs, min_length

