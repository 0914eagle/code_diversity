
def f1(n, m):
    # Calculate the number of subsequences of length n for each element in the range [1, m]
    num_subsequences = [0] * (m + 1)
    for i in range(1, m + 1):
        num_subsequences[i] = (i * (i + 1)) // 2

    # Calculate the sum of the number of subsequences for each sequence in S
    sum_subsequences = 0
    for i in range(1, m + 1):
        for j in range(i, m + 1):
            sum_subsequences = (sum_subsequences + num_subsequences[j] - num_subsequences[i - 1]) % (10**9 + 7)

    return sum_subsequences

def f2(n, m):
    # Calculate the number of subsequences of length n for each element in the range [1, m]
    num_subsequences = [0] * (m + 1)
    for i in range(1, m + 1):
        num_subsequences[i] = (i * (i + 1)) // 2

    # Calculate the sum of the number of subsequences for each sequence in S
    sum_subsequences = 0
    for i in range(1, m + 1):
        for j in range(i, m + 1):
            sum_subsequences = (sum_subsequences + num_subsequences[j] - num_subsequences[i - 1]) % (10**9 + 7)

    return sum_subsequences

if __name__ == '__main__':
    n, m = map(int, input().split())
    print(f1(n, m))

