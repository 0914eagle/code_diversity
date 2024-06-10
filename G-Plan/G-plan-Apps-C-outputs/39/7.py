
def longest_exploration_sequence(n, D, M, arr):
    def explore(start):
        visited = set()
        visited.add(start)
        current = arr[start]
        length = 1
        next_index = start + 1

        while next_index < n:
            if next_index - start > D or abs(arr[next_index] - current) > M or arr[next_index] in visited:
                break

            visited.add(next_index)
            current = arr[next_index]
            length += 1
            next_index += 1

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
