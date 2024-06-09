
def solve(s, t):
    # Initialize a dictionary to store the number of occurrences of each substring
    # of length |t| in s
    occurrences = {}

    # Iterate through each substring of length |t| in s
    for i in range(len(s) - len(t) + 1):
        substring = s[i:i+len(t)]

        # If the substring is already in the dictionary, increment its count
        if substring in occurrences:
            occurrences[substring] += 1

        # Otherwise, add the substring to the dictionary with count 1
        else:
            occurrences[substring] = 1

    # Return the maximum number of occurrences of t in s
    return max(occurrences.values())

