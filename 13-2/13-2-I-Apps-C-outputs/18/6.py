
def count_bulbasaurs(s):
    # Initialize a counter for the number of Bulbasaurs
    count = 0
    
    # Loop through the string s and check if we can form the word "Bulbasaur"
    for i in range(len(s)):
        # Check if the first letter is "B" and the second letter is "u"
        if s[i] == "B" and s[i+1] == "u":
            # Check if the third letter is "l" and the fourth letter is "b"
            if s[i+2] == "l" and s[i+3] == "b":
                # Check if the fifth letter is "a" and the sixth letter is "s"
                if s[i+4] == "a" and s[i+5] == "s":
                    # Check if the seventh letter is "a" and the eighth letter is "u"
                    if s[i+6] == "a" and s[i+7] == "u":
                        # If all conditions are met, increment the counter
                        count += 1
    
    # Return the number of Bulbasaurs found
    return count

