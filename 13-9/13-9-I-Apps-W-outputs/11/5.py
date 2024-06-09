
def solve(k):
    # Initialize the alphabet with its corresponding value
    alphabet = {chr(i): i for i in range(97, 123)}

    # Initialize the minimum length of the name
    min_length = 1

    # Initialize the name with the first letter
    name = "a"

    # Iterate until the name has the minimum length
    while len(name) < min_length:
        # Get the next letter in the alphabet
        next_letter = chr(ord(name[-1]) + 1)

        # Calculate the difference between the current letter and the next letter
        difference = abs(alphabet[name[-1]] - alphabet[next_letter])

        # Check if the difference is equal to the Sensei's favorite number
        if difference == k:
            # If it is, return the name
            return name + next_letter

        # If the difference is greater than the Sensei's favorite number,
        # increment the minimum length and try again
        if difference > k:
            min_length += 1

        # Add the next letter to the name and continue the loop
        name += next_letter

    # If no name has been found, return "impossible"
    return "impossible"

