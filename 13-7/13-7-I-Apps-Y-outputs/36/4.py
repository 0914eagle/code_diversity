
def get_longest_increasing_sequence(a):
    n = len(a)
    if n == 1:
        return 1, "R"
    
    # Initialize dp table with all 0s
    dp = [0] * (n + 1)
    dp[0] = 1
    
    # Loop through all elements of the array
    for i in range(1, n + 1):
        # Check if the current element is greater than the previous element
        if a[i - 1] > a[i - 2]:
            dp[i] = max(dp[i], dp[i - 1] + 1)
        else:
            dp[i] = max(dp[i], dp[i - 1])
    
    # Find the longest increasing subsequence
    max_len = max(dp)
    ans = ""
    i = n
    while i > 0 and dp[i] == max_len:
        if a[i - 1] > a[i - 2]:
            ans = "L" + ans
        else:
            ans = "R" + ans
        i -= 1
    
    return max_len, ans

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(get_longest_increasing_sequence(a))

if __name__ == '__main__':
    main()

