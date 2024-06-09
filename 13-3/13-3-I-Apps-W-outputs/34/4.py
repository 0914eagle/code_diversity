
def solve(n, a):
    # Initialize a dictionary to store the number of occurrences of each letter
    letter_counts = {}
    for i in range(n):
        letter_counts[i] = a[i]

    # Initialize a variable to store the maximum length of the string
    max_length = 0

    # Iterate through the dictionary and calculate the maximum length of the string
    for letter, count in letter_counts.items():
        max_length += count

    return max_length

