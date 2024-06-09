
def solve(s, t):
    # Initialize a dictionary to store the occurrences of each substring
    # in the string s
    occurrences = {}

    # Iterate through the string s and count the number of occurrences
    # of each substring
    for i in range(len(s)):
        substring = s[i:i+len(t)]
        if substring in occurrences:
            occurrences[substring] += 1
        else:
            occurrences[substring] = 1

    # Find the maximum number of occurrences of string t in string s
    max_occurrences = 0
    for substring, count in occurrences.items():
        if substring == t and count > max_occurrences:
            max_occurrences = count

    return max_occurrences

