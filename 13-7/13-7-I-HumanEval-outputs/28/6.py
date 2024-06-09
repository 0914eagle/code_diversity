
def is_bored(S: str) -> int:
    
    # Initialize a counter for the number of boredoms
    num_bored = 0
    
    # Split the input string into a list of sentences
    sentences = S.split('.')
    
    # Iterate through the list of sentences
    for sentence in sentences:
        # Check if the sentence starts with the word "I"
        if sentence.startswith('I'):
            # Increment the counter
            num_bored += 1
    
    # Return the number of boredoms
    return num_bored

