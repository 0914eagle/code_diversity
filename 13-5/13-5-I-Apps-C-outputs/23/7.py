
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

def find_critical_elements(sequence, length):
    n = len(sequence)
    critical_elements = []
    for i in range(n):
        if length == 1:
            break
        if sequence[i] not in critical_elements:
            length -= 1
            critical_elements.append(sequence[i])
    if length == 0:
        return "-1"
    return " ".join(str(element) for element in critical_elements)

def main():
    n, sequence = get_input()
    length = longest_increasing_subsequence(sequence)
    print(find_critical_elements(sequence, length))

if __name__ == '__main__':
    main()

