
def solve(s, p):
    # Initialize the answer array
    answer = [0] * (len(s) + 1)

    # Loop through each possible number of characters to remove
    for x in range(len(s)):
        # Remove x characters from the string
        s_prime = s[:len(s) - x]

        # Find the maximum number of non-overlapping substrings of p in s_prime
        max_occ = 0
        for i in range(len(s_prime) - len(p) + 1):
            if s_prime[i:i+len(p)] == p:
                max_occ += 1

        # Update the answer array
        answer[x] = max_occ

    return answer

