
def get_occurrences(s, p):
    # Initialize the maximum number of occurrences as 0
    max_occurrences = 0
    # Loop through the length of the string
    for i in range(len(s)):
        # Check if the substring starting from i with length equal to the pattern length is equal to the pattern
        if s[i:i+len(p)] == p:
            # If it is, increment the maximum number of occurrences
            max_occurrences += 1
    # Return the maximum number of occurrences
    return max_occurrences

def solve(s, p):
    # Initialize a list to store the answers
    answers = []
    # Loop through the length of the string
    for i in range(len(s)+1):
        # Get the substring of length i from the start of the string
        s_prime = s[:i]
        # Get the number of occurrences of the pattern in the substring
        occurrences = get_occurrences(s_prime, p)
        # Add the occurrences to the list of answers
        answers.append(occurrences)
    # Return the list of answers
    return answers

