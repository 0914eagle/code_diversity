
def get_node_order(n):
    # Initialize a list to store the node order
    node_order = []
    
    # Initialize a set to keep track of the disarmed nodes
    disarmed_nodes = set()
    
    # Start with node 0
    current_node = 0
    
    while len(disarmed_nodes) < n:
        # If the current node has already been disarmed, move on to the next node
        if current_node in disarmed_nodes:
            current_node = (current_node * 2) % n
            continue
        
        # Add the current node to the disarmed nodes set
        disarmed_nodes.add(current_node)
        
        # Add the current node to the node order list
        node_order.append(current_node)
        
        # Move on to the next node
        current_node = (current_node * 2) % n
    
    # If all nodes have been disarmed, return the node order list
    if len(disarmed_nodes) == n:
        return node_order
    
    # If not all nodes have been disarmed, return -1
    return -1

def main():
    n = int(input())
    node_order = get_node_order(n)
    if node_order == -1:
        print(-1)
    else:
        print(*node_order)

if __name__ == '__main__':
    main()

