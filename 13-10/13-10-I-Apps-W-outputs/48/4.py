
def find_order(n):
    # Initialize a list to store the order
    order = []
    
    # Add node 0 to the order
    order.append(0)
    
    # Iterate through the remaining nodes
    for i in range(1, n):
        # Find the next node to be disarmed
        next_node = (2 * order[i - 1]) % n
        
        # If the next node has already been disarmed, find the next available node
        while next_node in order:
            next_node = (next_node + 1) % n
        
        # Add the next node to the order
        order.append(next_node)
    
    # If the order is not complete, return -1
    if len(order) < n:
        return -1
    
    # Return the order
    return order

def main():
    # Read the input
    n = int(input())
    
    # Find the order
    order = find_order(n)
    
    # Print the order
    print(*order)

if __name__ == '__main__':
    main()

