
def longest_exploration_sequence(n, D, M, array):
    max_length = 0

    def explore(start):
        nonlocal max_length
        visited = set()
        visited.add(start)
        length = 1

        for i in range(start + 1, n):
            if abs(array[i] - array[start]) <= M and i - start <= D and array[i] not in visited:
                visited.add(i)
                length = max(length, 1 + explore(i))

        return length

    for i in range(n):
        max_length = max(max_length, explore(i))

    return max_length

if __name__ == "__main__":
    n, D, M = map(int, input().split())
    array = list(map(int, input().split()))
    print(longest_exploration_sequence(n, D, M, array))
