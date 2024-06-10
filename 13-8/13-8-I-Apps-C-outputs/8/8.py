
def get_longest_exploration_sequence(array, d, m):
    # Initialize variables
    n = len(array)
    visited = [False] * n
    longest = 0
    current = 0
    visited[current] = True

    # Iterate through the array
    for i in range(n):
        # Find the next unvisited element that is within the hopper's jump distance and value difference
        for j in range(current + 1, min(current + d + 1, n)):
            if not visited[j] and abs(array[j] - array[current]) <= m:
                current = j
                visited[current] = True
                longest = max(longest, j - current)
                break

    return longest

def main():
    # Read input
    n, d, m = map(int, input().split())
    array = list(map(int, input().split()))

    # Call the function
    longest = get_longest_exploration_sequence(array, d, m)

    # Print output
    print(longest)

if __name__ == '__main__':
    main()

