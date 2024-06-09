
def solve(n, x):
    # Initialize a list to store the nodes that are connected to the special node x
    connected_nodes = [x]
    # Iterate through the remaining nodes
    for i in range(1, n+1):
        # If the current node is not the special node x and it is connected to the special node x
        if i != x and i in connected_nodes:
            # Add the current node to the list of connected nodes
            connected_nodes.append(i)
    # If the list of connected nodes is equal to the number of nodes, then the special node is a leaf node and Ayush wins the game
    if len(connected_nodes) == n:
        return "Ayush"
    # Otherwise, Ashish wins the game
    else:
        return "Ashish"

