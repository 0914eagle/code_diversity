ore_array_length(n, D, M, arr):
    max_length = 0

    def explore(start, visited):
        nonlocal max_length
        max_length = max(max_length, len(visited))

        for i in range(start + 1, n):
            if abs(arr[i] - arr[start]) <= M and i - start <= D and i not in visited:
                explore(i, visited + [i])

    for i in range(n):
        explore(i, [i])

    return max_length


if __name__ == "__main__":
    n, D, M = map(int, input().split())
    arr = list(map(int, input().split()))

    result = explore_array_length(n, D, M, arr)
    print(result)
