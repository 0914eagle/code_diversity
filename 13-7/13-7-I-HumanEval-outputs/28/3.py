
def is_bored(S: str) -> int:
    
    # initialize a counter for boredoms
    boredoms = 0
    
    # split the input string into individual sentences
    sentences = S.split(".")
    
    # loop through each sentence
    for sentence in sentences:
        # check if the sentence starts with "I"
        if sentence.startswith("I"):
            # increase the counter by 1
            boredoms += 1
    
    # return the number of boredoms
    return boredoms

