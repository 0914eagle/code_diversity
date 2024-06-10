
def longest_exploration_sequence(n, D, M, arr):
    def explore(start):
        visited = set()
        visited.add(start)
        current = arr[start]
        length = 1

        for i in range(start + 1, n):
            if i in visited or abs(arr[i] - current) > M or i - start > D:
                break
            visited.add(i)
            current = arr[i]
            length += 1

        return length

    max_length = 0
    for i in range(n):
        max_length = max(max_length, explore(i))

    return max_length

if __name__ == "__main__":
    n, D, M = map(int, input().split())
    arr = list(map(int, input().split()))
    result = longest_exploration_sequence(n, D, M, arr)
    print(result)
