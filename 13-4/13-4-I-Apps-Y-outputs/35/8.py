
def solve_problem(n, k):
    # Initialize a list to store the letters of the alphabet
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    # Initialize an empty string to store the answer
    answer = ""
    
    # Loop through each letter of the alphabet
    for letter in alphabet:
        # Check if the letter is in the answer already
        if letter not in answer:
            # Add the letter to the answer
            answer += letter
            # Decrement the number of letters left to add
            n -= 1
            # If the number of letters left to add is 0, break the loop
            if n == 0:
                break
    
    # Return the answer
    return answer

