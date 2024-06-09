
def solve_problem(n, k):
    # Initialize a list to store the letters of the alphabet
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    # Initialize an empty string to store the result
    result = ""
    
    # Iterate through the alphabet and add each letter to the result string until the length of the result string is equal to n
    for letter in alphabet:
        if len(result) < n:
            result += letter
        else:
            break
    
    # If the length of the result string is greater than n, remove the last letter
    if len(result) > n:
        result = result[:-1]
    
    # Return the result string
    return result

