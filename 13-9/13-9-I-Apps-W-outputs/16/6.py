
def solve(s, p):
    # Initialize the answer array
    ans = [0] * (len(s) + 1)

    # Loop through each substring of s
    for i in range(len(s)):
        # Check if the substring is equal to p
        if s[i:i+len(p)] == p:
            # If it is, increment the answer by 1
            ans[i+1] = 1

    # Loop through each substring of s
    for i in range(len(s)):
        # Check if the substring is not equal to p
        if s[i:i+len(p)] != p:
            # If it is not, set the answer to the maximum of the previous answer and the current answer
            ans[i+1] = max(ans[i], ans[i+1])

    # Return the answer array
    return ans

