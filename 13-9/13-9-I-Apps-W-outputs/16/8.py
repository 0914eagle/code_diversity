
def solve(s, p):
    # Initialize the answer array
    ans = [0] * (len(s) + 1)

    # Loop through each substring of s
    for i in range(len(s)):
        # Check if the substring starts with p
        if s[i:i+len(p)] == p:
            # If it does, increment the answer for the corresponding substring length
            ans[i+1] += 1

    # Return the answer array
    return ans

