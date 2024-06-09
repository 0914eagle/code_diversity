
def f1(n, string):
    # Function to find the length of the longest alternating subsequence
    # in the given string
    length = len(string)
    dp = [0] * (length + 1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, length + 1):
        if string[i - 1] == string[i - 2]:
            dp[i] = dp[i - 1]
        else:
            dp[i] = max(dp[i - 1], dp[i - 2] + 1)
    return dp[length]

def f2(n, string):
    # Function to find the length of the longest alternating subsequence
    # in the given string after flipping a single substring
    length = len(string)
    dp = [0] * (length + 1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, length + 1):
        if string[i - 1] == string[i - 2]:
            dp[i] = max(dp[i - 1], dp[i - 2] + 1)
        else:
            dp[i] = dp[i - 1]
    return dp[length]

if __name__ == '__main__':
    n = int(input())
    string = input()
    print(f2(n, string))

