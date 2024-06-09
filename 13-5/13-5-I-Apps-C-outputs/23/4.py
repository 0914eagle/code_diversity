
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

def find_critical_elements(sequence, lis_length):
    n = len(sequence)
    critical_elements = []
    for i in range(n):
        if longest_increasing_subsequence(sequence[:i] + sequence[i+1:]) < lis_length:
            critical_elements.append(sequence[i])
    return critical_elements

def main():
    n, sequence = get_input()
    lis_length = longest_increasing_subsequence(sequence)
    critical_elements = find_critical_elements(sequence, lis_length)
    if not critical_elements:
        print(-1)
    else:
        print(*sorted(critical_elements))

if __name__ == '__main__':
    main()

