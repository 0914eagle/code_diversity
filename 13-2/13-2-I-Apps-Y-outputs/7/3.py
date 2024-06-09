
def solve(S, T):
    # Initialize a list to store the possible strings that satisfy Condition 1
    possible_strings = []

    # Iterate through all possible strings that are contiguous substrings of S
    for i in range(len(S) - len(T) + 1):
        # Check if the substring is equal to T
        if S[i:i+len(T)] == T:
            # If it is, add it to the list of possible strings
            possible_strings.append(S[i:i+len(T)])

    # If there are no possible strings, return "UNRESTORABLE"
    if not possible_strings:
        return "UNRESTORABLE"

    # Sort the list of possible strings in lexicographic order
    possible_strings.sort()

    # Return the first string in the list, which is the lexicographically smallest string that satisfies Condition 1
    return possible_strings[0]

