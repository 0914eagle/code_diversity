
def disarm(n):
    # Create a list to store the order
    order = [0]
    
    # Iterate through the nodes in the order
    for i in range(1, n):
        # Calculate the next node to disarm
        next_node = (2 * order[-1]) % n
        
        # If the next node has already been disarmed, calculate the next node
        while next_node in order:
            next_node = (next_node + 1) % n
        
        # Add the next node to the order
        order.append(next_node)
    
    # If the last node is not node 0, there is no solution
    if order[-1] != 0:
        return -1
    
    # Return the order
    return order

def main():
    n = int(input())
    order = disarm(n)
    print(" ".join(str(node) for node in order))

if __name__ == '__main__':
    main()

