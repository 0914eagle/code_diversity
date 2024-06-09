
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
    
    # Initialize an empty string to store the result
    result = ""
    
    # Iterate through each digit in S
    for digit in S:
        # If the digit is not in the dictionary, add it to the result as is
        if digit not in digit_map:
            result += digit
        # Otherwise, add the repeated version of the digit to the result
        else:
            result += digit_map[digit]
    
    # Return the K-th character from the left in the result string
    return result[K-1]

