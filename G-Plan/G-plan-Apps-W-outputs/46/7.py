
def check_possible_split(cookies):
    total_sum = sum(cookies)
    if total_sum % 2 != 0:
        return "No"

    target_sum = total_sum // 2
    dp = [False] * (target_sum + 1)
    dp[0] = True

    for cookie in cookies:
        for i in range(target_sum, cookie - 1, -1):
            dp[i] |= dp[i - cookie]

    return "Yes" if dp[target_sum] else "No"

if __name__ == '__main__':
    cookies = list(map(int, input().split()))
    print(check_possible_split(cookies))
