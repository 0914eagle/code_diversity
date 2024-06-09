
def count_bulbasaurs(s):
    # Initialize a counter for the number of Bulbasaurs
    count = 0
    
    # Loop through the string s and check if the substring "bulbasaur" can be formed
    for i in range(len(s) - 6):
        if s[i:i+7].lower() == "bulbasaur":
            count += 1
    
    # Return the number of Bulbasaurs
    return count

