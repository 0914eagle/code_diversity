
def count_bulbasaurs(s):
    # Initialize a counter for the number of Bulbasaurs
    count = 0
    
    # Loop through the string s and check if we can form the word "Bulbasaur"
    for i in range(len(s)):
        # Check if the first letter is uppercase "B"
        if s[i] == "B":
            # Check if the remaining letters form the word "ulbasaur"
            if s[i+1:i+8] == "ulbasaur":
                # Increment the counter
                count += 1
    
    # Return the number of Bulbasaurs
    return count

