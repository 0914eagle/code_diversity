
def disarm_nodes(n):
    # Initialize a list to store the order of nodes to be disarmed
    order = []
    
    # Start by disarming node 0
    order.append(0)
    
    # Loop through the remaining nodes
    for i in range(1, n):
        # Find the next node to be disarmed by checking the previous node
        # and following the rule given in the problem statement
        prev_node = order[i - 1]
        next_node = (2 * prev_node) % n
        if next_node == 0:
            next_node = (2 * prev_node) + 1
        
        # Add the next node to the order
        order.append(next_node)
    
    # Check if the order is valid by making sure that all nodes are disarmed exactly once
    if len(order) == n and len(set(order)) == n:
        return order
    else:
        return -1
    
def main():
    n = int(input("Enter the number of nodes: "))
    order = disarm_nodes(n)
    if order == -1:
        print("Impossible to disarm all nodes")
    else:
        print("Order to disarm nodes:", order)
    
if __name__ == '__main__':
    main()

