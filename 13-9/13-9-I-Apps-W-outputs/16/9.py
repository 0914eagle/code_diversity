
def solve(s, p):
    # Initialize the answer array
    answer = [0] * (len(s) + 1)

    # Loop through each possible number of removed characters
    for x in range(len(s)):
        # Get the substring of s after removing x characters
        s_prime = s[:len(s) - x]

        # Find the maximum number of non-overlapping substrings of p in s_prime
        max_occurrences = 0
        for i in range(len(s_prime) - len(p) + 1):
            if s_prime[i:i+len(p)] == p:
                max_occurrences += 1

        # Update the answer array for this x
        answer[x] = max_occurrences

    return answer
