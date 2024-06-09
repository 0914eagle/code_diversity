
def count_bulbasaurs(s):
    # Initialize a counter for the number of Bulbasaurs
    count = 0
    
    # Loop through the string s
    for i in range(len(s)):
        # Check if the substring starting at index i is "Bulbasaur"
        if s[i:i+8] == "Bulbasaur":
            # Increment the counter
            count += 1
    
    # Return the counter
    return count

