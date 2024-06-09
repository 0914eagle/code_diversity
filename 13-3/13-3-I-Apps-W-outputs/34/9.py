
def solve(n, a):
    # Initialize a dictionary to store the number of occurrences of each letter
    letter_counts = {}
    for i in range(n):
        letter_counts[i] = a[i]

    # Initialize a list to store the letters of the string
    string = []

    # Loop through the letters of the alphabet
    for letter in range(n):
        # If the letter has remaining occurrences, add it to the string
        if letter_counts[letter] > 0:
            string.append(letter)
            letter_counts[letter] -= 1

    # Return the length of the string
    return len(string)

