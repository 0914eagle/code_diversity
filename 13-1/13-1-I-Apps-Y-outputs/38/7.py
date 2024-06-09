
import sys

def is_possible(N, a):
    # Initialize the visited array with False
    visited = [False] * (N + 1)
    # Initialize the queue with Button 1
    queue = [1]
    # Loop until the queue is empty
    while queue:
        # Get the current button from the queue
        current = queue.pop(0)
        # If the current button is Button 2, return True
        if current == 2:
            return True
        # If the current button is not visited, mark it as visited and add its neighbor to the queue
        if not visited[current]:
            visited[current] = True
            queue.append(a[current - 1])
    # If we reach here, it means we couldn't find Button 2, so return False
    return False

# Read the input from stdin
N = int(input())
a = list(map(int, input().split()))
# Check if it is possible to lighten up Button 2
if is_possible(N, a):
    # If it is possible, find the minimum number of times we need to press buttons
    count = 0
    current = 1
    while current != 2:
        count += 1
        current = a[current - 1]
    print(count)
else:
    print(-1)

