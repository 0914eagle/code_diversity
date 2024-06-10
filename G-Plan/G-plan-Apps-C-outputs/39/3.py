
def longest_exploration_sequence(n, D, M, arr):
    max_length = 0

    for i in range(n):
        for j in range(i, n):
            if abs(arr[j] - arr[i]) <= M and j - i <= D:
                max_length = max(max_length, j - i + 1)

    return max_length

if __name__ == "__main__":
    n, D, M = map(int, input().split())
    arr = list(map(int, input().split()))

    result = longest_exploration_sequence(n, D, M, arr)
    print(result)
