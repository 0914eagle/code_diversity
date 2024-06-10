
def get_order(n):
    # Initialize a list to store the order
    order = [0]
    
    # Iterate from 1 to n-1
    for i in range(1, n):
        # Find the next node to disarm
        next_node = (2*order[-1]) % n
        
        # If the next node is already in the order, find the next one
        while next_node in order:
            next_node = (next_node + 1) % n
            
        # Add the next node to the order
        order.append(next_node)
    
    # If the order is not complete, return -1
    if len(order) != n:
        return -1
    
    # Return the order
    return order

def main():
    n = int(input())
    order = get_order(n)
    print(" ".join(str(node) for node in order))

if __name__ == '__main__':
    main()

