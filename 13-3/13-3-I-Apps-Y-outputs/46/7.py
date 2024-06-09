
def solve(s, k):
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
    
    # Loop through each character in the input string
    for char in s:
        # If the character is a digit, replace it with its repeated version
        if char in digit_map:
            result += digit_map[char]
        # If the character is not a digit, add it to the result as is
        else:
            result += char
    
    # Return the K-th character from the left in the result string
    return result[k-1]

