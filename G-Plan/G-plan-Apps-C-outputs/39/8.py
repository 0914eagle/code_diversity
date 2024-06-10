
def longest_exploration_sequence(n, D, M, arr):
    max_length = 0

    def explore_sequence(start):
        nonlocal max_length
        visited = set()
        visited.add(start)
        length = 1
        current = start

        while True:
            next_found = False
            for i in range(current + 1, min(n, current + D + 1)):
                if abs(arr[i] - arr[current]) <= M and i not in visited:
                    visited.add(i)
                    current = i
                    length += 1
                    next_found = True
                    break

            if not next_found:
                break

        max_length = max(max_length, length)

    for i in range(n):
        explore_sequence(i)

    return max_length

if __name__ == "__main__":
    n, D, M = map(int, input().split())
    arr = list(map(int, input().split()))
    result = longest_exploration_sequence(n, D, M, arr)
    print(result)
