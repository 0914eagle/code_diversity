
def solve(s, t):
    # Initialize a dictionary to store the number of occurrences of each substring
    # of length |t| in s
    occurrences = {}

    # Iterate through each substring of length |t| in s
    for i in range(len(s) - len(t) + 1):
        substring = s[i:i+len(t)]

        # If the substring is not already in the dictionary, add it and initialize its count to 0
        if substring not in occurrences:
            occurrences[substring] = 0

        # Increment the count of the substring
        occurrences[substring] += 1

    # Find the maximum number of occurrences of t in s
    max_occurrences = max(occurrences.values())

    # Return the maximum number of occurrences
    return max_occurrences

