
def get_input():
    n, T = map(int, input().split())
    a = list(map(int, input().split()))
    return n, T, a

def longest_non_decreasing_sequence(a):
    n = len(a)
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if a[i] >= a[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

def main():
    n, T, a = get_input()
    print(longest_non_decreasing_sequence(a))

if __name__ == '__main__':
    main()

