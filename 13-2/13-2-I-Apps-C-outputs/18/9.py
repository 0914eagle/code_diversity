
def count_bulbasaurs(text):
    # Initialize a counter for the number of Bulbasaurs
    count = 0
    
    # Loop through the text and check if we can form the word "Bulbasaur"
    for i in range(len(text)):
        # Check if the first letter is "B" and the second letter is "u"
        if text[i] == "B" and text[i+1] == "u":
            # Check if the third letter is "l" and the fourth letter is "b"
            if text[i+2] == "l" and text[i+3] == "b":
                # Check if the fifth letter is "a" and the sixth letter is "s"
                if text[i+4] == "a" and text[i+5] == "s":
                    # Check if the seventh letter is "a" and the eighth letter is "u"
                    if text[i+6] == "a" and text[i+7] == "u":
                        # If all conditions are met, increment the counter
                        count += 1
    
    # Return the number of Bulbasaurs found
    return count

