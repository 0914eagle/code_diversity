
def get_input():
    n = int(input())
    sequence = list(map(int, input().split()))
    return n, sequence

def longest_increasing_subsequence(sequence):
    n = len(sequence)
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if sequence[i] > sequence[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
    return max(dp)

def critical_elements(sequence):
    n = len(sequence)
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if sequence[i] > sequence[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
    critical = []
    for i in range(n):
        if dp[i] == 1:
            critical.append(sequence[i])
    return critical

def main():
    n, sequence = get_input()
    print(*critical_elements(sequence), sep='\n')

if __name__ == '__main__':
    main()

