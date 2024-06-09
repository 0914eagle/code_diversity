
from typing import Dict

def histogram(test: str) -> Dict[str, int]:
    
    # Initialize an empty dictionary to store the histogram
    hist = {}
    
    # Split the input string into a list of words
    words = test.split()
    
    # Iterate over the list of words
    for word in words:
        # Check if the word is already in the histogram
        if word in hist:
            # If it is, increment its count
            hist[word] += 1
        else:
            # If it's not, add it to the histogram with a count of 1
            hist[word] = 1
    
    # Return the histogram
    return hist

