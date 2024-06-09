
def solve(N, A, B):
    # Initialize a dictionary to store the debts
    debts = {}

    # Loop through the input and add the debts to the dictionary
    for i in range(N):
        debts[i + 1] = -B[i]

    # Loop through the input and add the debts to the dictionary
    for i in range(N):
        debts[A[i]] += B[i]

    # Initialize a set to store the visited nodes
    visited = set()

    # Initialize a queue to store the nodes to visit
    queue = []

    # Add the node with the maximum debt to the queue
    queue.append(max(debts, key=debts.get))

    # Loop until the queue is empty
    while queue:
        # Get the current node from the queue
        node = queue.pop(0)

        # If the node has already been visited, skip it
        if node in visited:
            continue

        # Mark the node as visited
        visited.add(node)

        # Get the debt of the current node
        debt = debts[node]

        # If the debt is positive, add it to the total amount of money the town has to give
        if debt > 0:
            total_amount += debt

        # Loop through the neighbors of the current node
        for neighbor in debts:
            # If the neighbor has not been visited and has a positive debt, add it to the queue
            if neighbor not in visited and debts[neighbor] > 0:
                queue.append(neighbor)

    # Return the total amount of money the town has to give
    return total_amount

