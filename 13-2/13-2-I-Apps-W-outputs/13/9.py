
def get_min_operations(balances):
    # Initialize a queue to store the banks to visit
    queue = []
    # Initialize a dictionary to store the minimum number of operations required to make the balance zero for each bank
    min_operations = {}
    # Initialize a set to store the visited banks
    visited = set()

    # Enqueue the first bank and set the minimum number of operations required to zero
    queue.append(0)
    min_operations[0] = 0

    # Loop until the queue is empty
    while queue:
        # Dequeue a bank and its minimum number of operations required to make the balance zero
        bank, operations = queue.pop(0)

        # If the bank has already been visited, skip it
        if bank in visited:
            continue

        # Mark the bank as visited
        visited.add(bank)

        # Get the balance of the bank
        balance = balances[bank]

        # If the balance is zero, we have found the minimum number of operations required to make the balance zero for this bank
        if balance == 0:
            min_operations[bank] = operations
            continue

        # Otherwise, find the neighboring bank with the minimum balance that is not visited yet
        min_balance = float('inf')
        min_neighbor = -1
        for neighbor in get_neighbors(bank, len(balances)):
            if neighbor not in visited and balances[neighbor] < min_balance:
                min_balance = balances[neighbor]
                min_neighbor = neighbor

        # If a neighboring bank with a non-zero balance has been found, enqueue it and set the minimum number of operations required to make the balance zero for this bank
        if min_neighbor != -1:
            queue.append((min_neighbor, operations + 1))
            min_operations[min_neighbor] = operations + 1

    # Return the minimum number of operations required to make the balance zero for each bank
    return min_operations

def get_neighbors(bank, n):
    # Get the indices of the neighboring banks
    neighbors = [bank - 1, bank + 1]
    if bank == 0:
        neighbors.append(n - 1)
    elif bank == n - 1:
        neighbors.append(0)

    return neighbors

if __name__ == '__main__':
    balances = [5, 0, -5]
    print(get_min_operations(balances))

