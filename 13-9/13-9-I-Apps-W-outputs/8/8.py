
import sys
input = sys.stdin.read()

def get_tree_data(input_data):
    # split the input data into lines
    lines = input_data.split('\n')
    
    # get the number of vertices and edges
    num_vertices, num_edges = map(int, lines[0].split())
    
    # create a dictionary to store the tree data
    tree_data = {}
    
    # iterate over the edges
    for i in range(1, num_edges + 1):
        # split the edge data
        edge = lines[i].split()
        
        # add the edge to the tree data
        tree_data[i] = (int(edge[0]), int(edge[1]))
    
    return num_vertices, num_edges, tree_data

def get_initial_counters(num_vertices):
    # create a list to store the initial counters
    counters = [0] * (num_vertices + 1)
    
    # return the initial counters
    return counters

def perform_operations(num_vertices, num_edges, tree_data, counters, operations):
    # iterate over the operations
    for operation in operations:
        # get the root of the subtree and the increment value
        root, increment = operation
        
        # recursively traverse the subtree, updating the counters
        recursively_update_counters(root, increment, tree_data, counters)
    
    # return the updated counters
    return counters

def recursively_update_counters(vertex, increment, tree_data, counters):
    # update the counter for the current vertex
    counters[vertex] += increment
    
    # check if the current vertex is a leaf
    if vertex not in tree_data:
        return
    
    # recursively traverse the subtree, updating the counters
    for child in tree_data[vertex]:
        recursively_update_counters(child, increment, tree_data, counters)

def print_counters(counters):
    # print the counters
    for counter in counters:
        print(counter, end=' ')

# get the tree data
num_vertices, num_edges, tree_data = get_tree_data(input)

# get the initial counters
counters = get_initial_counters(num_vertices)

# perform the operations
operations = [tuple(map(int, line.split())) for line in input.split('\n')[num_edges + 1:]]
counters = perform_operations(num_vertices, num_edges, tree_data, counters, operations)

# print the counters
print_counters(counters)

