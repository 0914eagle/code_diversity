
def is_bored(S: str) -> int:
    
    # Initialize a counter for the number of boredoms
    count = 0
    
    # Split the input string into individual sentences
    sentences = S.split(".")
    
    # Iterate over the sentences
    for sentence in sentences:
        # Check if the sentence starts with "I"
        if sentence.startswith("I"):
            # Increment the counter
            count += 1
    
    # Return the number of boredoms
    return count
