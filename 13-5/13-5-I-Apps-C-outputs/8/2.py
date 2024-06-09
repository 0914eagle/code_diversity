
def f1(n, string):
    # Calculate the length of the longest alternating subsequence
    # by dynamic programming
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        if string[i - 1] == '0':
            dp[i] = max(dp[i - 1], dp[i - 2] + 1)
        else:
            dp[i] = max(dp[i - 1], dp[i - 2])
    return dp[n]

def f2(n, string):
    # Find the longest substring of consecutive '0's or '1's
    # and flip it to create the longest alternating subsequence
    longest = 0
    for i in range(n):
        if string[i] == '0':
            j = i + 1
            while j < n and string[j] == '0':
                j += 1
            longest = max(longest, j - i)
        elif string[i] == '1':
            j = i + 1
            while j < n and string[j] == '1':
                j += 1
            longest = max(longest, j - i)
    return longest

if __name__ == '__main__':
    n = int(input())
    string = input()
    print(f2(n, string))

