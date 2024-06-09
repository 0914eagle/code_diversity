
def solve(S, queries):
    # Initialize a dictionary to store the count of AC as a substring
    ac_count = {}

    # Iterate through the string S
    for i in range(len(S)):
        # Check if the current substring starting at index i is AC
        if S[i:i+2] == "AC":
            # If it is, increment the count for this substring
            if i in ac_count:
                ac_count[i] += 1
            else:
                ac_count[i] = 1

    # Initialize an empty list to store the answers
    answers = []

    # Iterate through the queries
    for l, r in queries:
        # Check if the current query is valid
        if l > r or l < 1 or r > len(S):
            answers.append(-1)
            continue

        # Initialize a variable to store the count for the current query
        count = 0

        # Iterate through the substrings starting at index l and ending at index r
        for i in range(l, r+1):
            # Check if the current substring is AC
            if S[i:i+2] == "AC":
                # If it is, increment the count
                count += 1

        # Add the count to the list of answers
        answers.append(count)

    return answers

