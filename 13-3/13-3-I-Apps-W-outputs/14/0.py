
def f1(n, k, a):
    # Initialize a dictionary to store the number of good arrays for each position
    dp = {0: 1}
    for i in range(n):
        # If the current element is -1, we can replace it with any number from 1 to k
        if a[i] == -1:
            for j in range(1, k+1):
                # If the current position is not in the dictionary, initialize it to 0
                if i not in dp:
                    dp[i] = 0
                # Add the number of good arrays obtained by replacing the current element with j
                dp[i] += dp.get(i-1, 0)
        # If the current element is not -1, we can only replace it with itself
        else:
            if i not in dp:
                dp[i] = 0
            dp[i] += dp.get(i-1, 0)
    # Return the number of good arrays for the last position
    return dp[n-1]

def f2(n, k, a):
    # Initialize a dictionary to store the number of good arrays for each position
    dp = {0: 1}
    for i in range(n):
        # If the current element is -1, we can replace it with any number from 1 to k
        if a[i] == -1:
            for j in range(1, k+1):
                # If the current position is not in the dictionary, initialize it to 0
                if i not in dp:
                    dp[i] = 0
                # Add the number of good arrays obtained by replacing the current element with j
                dp[i] += dp.get(i-1, 0)
        # If the current element is not -1, we can only replace it with itself
        else:
            if i not in dp:
                dp[i] = 0
            dp[i] += dp.get(i-1, 0)
    # Return the number of good arrays for the last position
    return dp[n-1]

if __name__ == '__main__':
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(f1(n, k, a))

