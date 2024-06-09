
def read_sequence():
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
    dp = [False] * n
    for i in range(n):
        if lis_length == 1:
            break
        for j in range(i):
            if sequence[i] > sequence[j] and dp[j] == False and lis_length == dp[j] + 1:
                dp[i] = True
                lis_length -= 1
                break
    return [sequence[i] for i in range(n) if dp[i]]

def main():
    n, sequence = read_sequence()
    lis_length = longest_increasing_subsequence(sequence)
    critical_elements = find_critical_elements(sequence, lis_length)
    if len(critical_elements) == 0:
        print(-1)
    else:
        print(*critical_elements)

if __name__ == '__main__':
    main()

