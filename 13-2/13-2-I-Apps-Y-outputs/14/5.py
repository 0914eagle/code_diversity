
def get_max_divisible_numbers(s):
    n = len(s)
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        if s[i - 1] == '3':
            dp[i] = dp[i - 1] + 1
        else:
            dp[i] = dp[i - 1]
    return dp[n]

def main():
    s = input()
    print(get_max_divisible_numbers(s))

if __name__ == '__main__':
    main()

