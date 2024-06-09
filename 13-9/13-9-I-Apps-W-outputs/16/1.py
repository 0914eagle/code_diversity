
def solve(s, p):
    # Initialize the answer array
    answer = [0] * (len(s) + 1)

    # Loop through each possible removal length
    for x in range(len(s)):
        # Remove x characters from the string
        s_prime = s[:x] + s[x + 1:]

        # Calculate the number of non-overlapping substrings of p in s'
        occ = 0
        while s_prime.find(p) != -1:
            occ += 1
            s_prime = s_prime[s_prime.find(p) + 1:]

        # Update the answer array
        answer[x] = max(answer[x], occ)

    return answer

