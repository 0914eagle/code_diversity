
def solve(n, f):
    # Initialize a list to store the answers
    ans = [0] * n

    # Iterate through the input and fill in the answers
    for i in range(n):
        # If the current friend doesn't know whom to give the gift to, find the next available friend
        if f[i] == 0:
            for j in range(1, n + 1):
                if j != i and ans[j - 1] == 0:
                    ans[i] = j
                    ans[j - 1] = i + 1
                    break
        # If the current friend knows whom to give the gift to, find the next available friend who doesn't know whom to give the gift to
        else:
            for j in range(1, n + 1):
                if j != i and ans[j - 1] == 0 and f[j - 1] != 0:
                    ans[i] = j
                    ans[j - 1] = i + 1
                    break

    # Return the answers
    return ans

