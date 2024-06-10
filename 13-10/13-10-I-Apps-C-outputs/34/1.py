
import sys

MOD = 10**9 + 7

def read_input():
    N = int(input())
    S = input()
    return N, S

def count_palindromes(S, N):
    count = 0
    for i in range(len(S)):
        sub_str = S[i:i+N]
        if sub_str == sub_str[::-1]:
            count += 1
    return count

def count_palindromes_recursive(S, N):
    if N == 0:
        return 1
    if N == 1:
        return 26
    count = 0
    for i in range(26):
        sub_str = S[i:i+N-1]
        count += count_palindromes_recursive(sub_str, N-1)
    return count

def count_palindromes_dp(S, N):
    dp = [0] * (N+1)
    dp[0] = 1
    dp[1] = 26
    for i in range(2, N+1):
        for j in range(26):
            sub_str = S[j:j+i-1]
            dp[i] += dp[i-1]
    return dp[N]

def main():
    N, S = read_input()
    print(count_palindromes(S, N) % MOD)
    # print(count_palindromes_recursive(S, N) % MOD)
    # print(count_palindromes_dp(S, N) % MOD)

if __name__ == '__main__':
    main()

