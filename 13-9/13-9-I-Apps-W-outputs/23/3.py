
def cut_into_good_substrings(s):
    n = len(s)
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        if s[i - 1] == '0':
            dp[i] = dp[i - 1] + 1
        else:
            dp[i] = dp[i - 1]
    k = 0
    while dp[n] > 0:
        k += 1
        n -= dp[n]
    return k

def get_good_substrings(s, k):
    n = len(s)
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        if s[i - 1] == '0':
            dp[i] = dp[i - 1] + 1
        else:
            dp[i] = dp[i - 1]
    substrings = []
    while k > 0:
        substrings.append(s[:dp[n]])
        s = s[dp[n]:]
        n -= dp[n]
        k -= 1
    return substrings

if __name__ == '__main__':
    n = int(input())
    s = input()
    k = cut_into_good_substrings(s)
    substrings = get_good_substrings(s, k)
    print(k)
    print(*substrings)

