
def solve(s, p):
    # Initialize the answer array
    answer = [0] * (len(s) + 1)

    # Loop through each possible number of characters to remove
    for x in range(len(s)):
        # Remove x characters from the end of the string
        s_prime = s[:len(s) - x]

        # Count the number of non-overlapping substrings equal to p in s_prime
        count = 0
        while s_prime.find(p) != -1:
            count += 1
            s_prime = s_prime[s_prime.find(p) + len(p):]

        # Update the answer for this number of characters removed
        answer[x] = count

    return answer

