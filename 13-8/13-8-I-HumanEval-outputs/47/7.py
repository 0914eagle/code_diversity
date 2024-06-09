
def is_bored(S: str) -> int:
    
    # initialize a counter for boredoms
    boredoms = 0
    
    # split the input string into sentences
    sentences = S.split('.')
    
    # loop through each sentence
    for sentence in sentences:
        # check if the sentence starts with "I"
        if sentence.startswith('I'):
            # increment the counter
            boredoms += 1
    
    # return the number of boredoms
    return boredoms

