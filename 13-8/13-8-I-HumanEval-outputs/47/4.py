
def is_bored(S: str) -> int:
    
    # Initialize a counter for the number of boredoms
    boredom_count = 0
    
    # Split the input string into sentences
    sentences = S.split(".")
    
    # Iterate through the sentences
    for sentence in sentences:
        # Check if the sentence starts with "I"
        if sentence.startswith("I"):
            # Increment the boredom count
            boredom_count += 1
    
    # Return the boredom count
    return boredom_count

