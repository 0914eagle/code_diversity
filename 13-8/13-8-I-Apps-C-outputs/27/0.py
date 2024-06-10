
import sys

def get_input():
    n = int(input())
    numbers = []
    for i in range(n):
        numbers.append(int(input()))
    return n, numbers

def find_common_factors(x, y):
    factors = []
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0 and y % i == 0:
            factors.append(i)
    return factors

def count_ways(numbers):
    n = len(numbers)
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        for j in range(i):
            common_factors = find_common_factors(numbers[i - 1], numbers[j])
            if common_factors:
                dp[i] += dp[j]
        dp[i] %= 1000000007
    return dp[n]

def main():
    n, numbers = get_input()
    print(count_ways(numbers))

if __name__ == '__main__':
    main()

