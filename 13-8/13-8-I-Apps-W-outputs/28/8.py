
def get_minimal_bdd_vertices(n, function_values):
    # Initialize a dictionary to store the BDD nodes
    nodes = {}
    
    # Initialize the root node with the function values
    root = Node(0, function_values)
    nodes[0] = root
    
    # Iterate until there are no more nodes to process
    while len(nodes) > 0:
        # Get the next node to process
        node = nodes.pop(0)
        
        # If the node is a leaf node, we are done
        if node.is_leaf:
            continue
        
        # Get the child nodes for the current node
        child_nodes = node.get_child_nodes()
        
        # Add the child nodes to the dictionary
        for child_node in child_nodes:
            nodes[child_node.index] = child_node
    
    # Return the number of vertices in the BDD
    return len(nodes) + 1

# Node class to represent a node in the BDD
class Node:
    def __init__(self, index, values):
        self.index = index
        self.values = values
        self.is_leaf = False
    
    # Get the child nodes for the current node
    def get_child_nodes(self):
        child_nodes = []
        
        # Iterate over the possible values for the current node
        for i in range(len(self.values)):
            # Create a new node for the child
            child_node = Node(self.index * 2 + i, self.values[i])
            
            # Add the child node to the list of child nodes
            child_nodes.append(child_node)
        
        return child_nodes

