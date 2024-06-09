
def is_bored(S: str) -> int:
    
    # Initialize a counter for the number of boredoms
    num_boredoms = 0
    
    # Split the input string into a list of sentences
    sentences = S.split(".")
    
    # Loop through each sentence
    for sentence in sentences:
        # Check if the sentence starts with "I"
        if sentence.startswith("I"):
            # Increment the counter
            num_boredoms += 1
    
    # Return the number of boredoms
    return num_boredoms

