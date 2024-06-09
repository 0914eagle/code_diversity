
def is_bored(S: str) -> int:
    
    # Initialize a counter for boredoms
    boredoms = 0
    
    # Split the input string into individual sentences
    sentences = S.split(".")
    
    # Iterate through each sentence
    for sentence in sentences:
        # Check if the sentence starts with "I"
        if sentence.strip().startswith("I"):
            # Increment the counter for boredoms
            boredoms += 1
    
    # Return the number of boredoms
    return boredoms

