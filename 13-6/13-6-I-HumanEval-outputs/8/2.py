
def is_bored(S: str) -> int:
    
    # Initialize a counter for the number of boredoms
    boredom_count = 0
    
    # Split the input string into individual sentences
    sentences = S.split(".")
    
    # Loop through each sentence
    for sentence in sentences:
        # Check if the sentence starts with "I"
        if sentence.startswith("I"):
            # Increment the boredom counter
            boredom_count += 1
    
    # Return the number of boredoms
    return boredom_count

