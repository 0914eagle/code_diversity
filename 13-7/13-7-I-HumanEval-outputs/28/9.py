
def is_bored(S: str) -> int:
    
    # Initialize a counter for the number of boredoms
    num_boredoms = 0
    
    # Split the input string into individual sentences
    sentences = S.split(".")
    
    # Iterate through the sentences
    for sentence in sentences:
        # Check if the sentence starts with "I"
        if sentence.strip().startswith("I"):
            # Increment the counter
            num_boredoms += 1
    
    # Return the number of boredoms
    return num_boredoms

