
def solve(n, accounts):
    # Initialize a queue to store the banks to visit
    queue = []
    
    # Initialize a dictionary to store the minimum number of operations required to make the balance zero for each bank
    balance = {}
    
    # Initialize a set to store the visited banks
    visited = set()
    
    # Enqueue the first bank and set the minimum number of operations required to zero
    queue.append(0)
    balance[0] = 0
    
    # Loop until the queue is empty
    while queue:
        # Dequeue a bank and get its balance
        bank = queue.pop(0)
        current_balance = accounts[bank]
        
        # If the balance is zero, we have found the minimum number of operations required to make the balance zero for this bank
        if current_balance == 0:
            continue
        
        # Get the neighbors of the current bank
        neighbors = get_neighbors(n, bank)
        
        # Loop through the neighbors and enqueue them if they have not been visited yet
        for neighbor in neighbors:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
                balance[neighbor] = current_balance
        
    # Return the minimum number of operations required to make the balance zero for each bank
    return [balance[i] for i in range(n)]

def get_neighbors(n, bank):
    # Get the neighbors of the current bank
    neighbors = [bank - 1, bank + 1]
    
    # If the bank is the first or last bank, add the last bank as a neighbor
    if bank == 0:
        neighbors.append(n - 1)
    elif bank == n - 1:
        neighbors.append(0)
    
    return neighbors

