
def get_min_turns(n, A, B, left_turns, right_turns):
    # Initialize a queue to store the paths
    queue = [(A, 0)]

    # Initialize a set to keep track of the visited nodes
    visited = set()

    # Initialize the minimum number of turns to be infinity
    min_turns = float('inf')

    # Loop until the queue is empty
    while queue:
        # Get the current node and the number of turns
        node, turns = queue.pop(0)

        # If the node is the destination node, update the minimum number of turns
        if node == B:
            min_turns = min(min_turns, turns)
            continue

        # If the node has already been visited, skip it
        if node in visited:
            continue

        # Mark the node as visited
        visited.add(node)

        # Get the left and right turns for the current node
        left = left_turns[node]
        right = right_turns[node]

        # If the left turn is not None, add it to the queue
        if left is not None:
            queue.append((left, turns + 1))

        # If the right turn is not None, add it to the queue
        if right is not None:
            queue.append((right, turns + 1))

    # Return the minimum number of turns
    return min_turns

def main():
    # Read the input
    n, A, B = map(int, input().split())
    left_turns = [None] * n
    right_turns = [None] * n
    for i in range(n):
        l, r, t = map(int, input().split())
        left_turns[i] = l
        right_turns[i] = r

    # Call the get_min_turns function
    min_turns = get_min_turns(n, A, B, left_turns, right_turns)

    # Print the result
    if min_turns == float('inf'):
        print("indistinguishable")
    else:
        print(min_turns)

if __name__ == '__main__':
    main()

