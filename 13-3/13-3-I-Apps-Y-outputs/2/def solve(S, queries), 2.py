
def solve(S, queries):
    # Initialize a dictionary to store the count of AC as a substring
    ac_count = {}

    # Iterate through the string S
    for i in range(len(S)):
        # Check if the current substring starting at index i is AC
        if S[i:i+2] == "AC":
            # If it is, increment the count for this substring
            if i+2 not in ac_count:
                ac_count[i+2] = 1
            else:
                ac_count[i+2] += 1

    # Initialize an empty list to store the answers
    answers = []

    # Iterate through the queries
    for l, r in queries:
        # Check if the substring starting at index l and ending at index r is a substring of S
        if l <= r and r <= len(S):
            # If it is, add the count of AC as a substring for this substring to the list of answers
            answers.append(ac_count[l] if l in ac_count else 0)
        else:
            # If it is not, add 0 to the list of answers
            answers.append(0)

    return answers

