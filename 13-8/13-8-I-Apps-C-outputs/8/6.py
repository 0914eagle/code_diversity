
def get_longest_exploration_sequence(array, d, m):
    # Initialize variables
    n = len(array)
    visited = [False] * n
    longest = 0
    for i in range(n):
        if not visited[i]:
            # Visit the current element and mark it as visited
            visited[i] = True
            # Calculate the longest exploration sequence starting from the current element
            longest = max(longest, explore(array, visited, i, d, m) + 1)
    return longest

def explore(array, visited, i, d, m):
    # Base case: if we reach the end of the array, return 0
    if i == len(array) - 1:
        return 0
    # Initialize variables
    j = i + 1
    while j < len(array) and abs(array[i] - array[j]) <= m:
        j += 1
    # If we can jump to the next element, mark it as visited and calculate the longest exploration sequence starting from the next element
    if j < len(array) and j - i <= d:
        visited[j] = True
        return explore(array, visited, j, d, m)
    # Otherwise, return 0
    else:
        return 0

if __name__ == '__main__':
    n, d, m = map(int, input().split())
    array = list(map(int, input().split()))
    print(get_longest_exploration_sequence(array, d, m))

