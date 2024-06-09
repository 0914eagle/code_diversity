
def get_longest_common_subsequence(s1, s2, virus):
    m = len(s1)
    n = len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m):
        for j in range(n):
            if s1[i] == s2[j] and s1[i] not in virus:
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
    return "".join(s1[i - dp[i][-1]:i])

def main():
    s1 = input()
    s2 = input()
    virus = input()
    print(get_longest_common_subsequence(s1, s2, virus))

if __name__ == '__main__':
    main()

