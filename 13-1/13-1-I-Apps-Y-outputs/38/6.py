
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

def get_min_presses(N, a):
    # Initialize the minimum number of presses to infinity
    min_presses = float('inf')
    # Loop through all possible starting buttons
    for i in range(1, N + 1):
        # If the current button is lighten up, try to find Button 2 from there
        if is_possible(N, a):
            # If we found Button 2, update the minimum number of presses
            min_presses = min(min_presses, i)
    # Return the minimum number of presses
    return min_presses

N = int(input())
a = list(map(int, input().split()))
print(get_min_presses(N, a))

