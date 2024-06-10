
def get_circuit_order(n):
    # Initialize a list to store the order
    order = []
    
    # Add node 0 to the order
    order.append(0)
    
    # Iterate through the remaining nodes
    for i in range(1, n):
        # Find the next node to be disarmed
        next_node = (2 * order[-1]) % n
        
        # If the next node has already been disarmed, find the other option
        if next_node in order:
            next_node = (2 * order[-1]) + 1 % n
        
        # Add the next node to the order
        order.append(next_node)
    
    # If the order is not complete, return -1
    if len(order) != n:
        return -1
    
    # Return the order
    return order

def main():
    # Read the input
    n = int(input())
    
    # Get the circuit order
    order = get_circuit_order(n)
    
    # Print the order
    print(*order)

if __name__ == '__main__':
    main()

