
def solve(S, K):
    # Initialize a dictionary to map each digit to its repeated version
    digit_map = {
        "1": "1",
        "2": "22",
        "3": "333",
        "4": "4444",
        "5": "55555",
        "6": "666666",
        "7": "7777777",
        "8": "88888888",
        "9": "999999999"
    }
    
    # Initialize a variable to store the length of the string after 5*10^15 days
    length = 0
    
    # Iterate through each day
    for day in range(5*10**15):
        # Initialize a new string to store the updated string for the current day
        updated_string = ""
        
        # Iterate through each character in the current string
        for char in S:
            # Check if the character is a digit
            if char.isdigit():
                # Replace the digit with its repeated version using the dictionary
                updated_string += digit_map[char]
            else:
                # If the character is not a digit, add it to the updated string as is
                updated_string += char
        
        # Update the length of the string after the current day
        length += len(updated_string)
        
        # Check if the length of the string after the current day is greater than or equal to K
        if length >= K:
            # If it is, return the K-th character from the left in the string
            return updated_string[K-1]
        
        # Update the current string for the next day
        S = updated_string
    
    # If we reach this point, it means that the length of the string after 5*10^15 days is less than K
    return -1

