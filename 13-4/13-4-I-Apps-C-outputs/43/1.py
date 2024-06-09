
def solve(A, B):
    # Find the minimum cost to cut B out of A
    cost = 0
    
    # Iterate through the edges of B
    for i in range(len(B)):
        # Find the edge of B and the corresponding edge of A
        edge_B = B[i]
        edge_A = find_corresponding_edge(A, edge_B)
        
        # Calculate the length of the cut
        length = calculate_length(edge_A, edge_B)
        
        # Add the length to the total cost
        cost += length
    
    return cost

def find_corresponding_edge(A, edge):
    # Find the edge in A that is closest to the given edge
    min_distance = float('inf')
    corresponding_edge = None
    for edge_A in A:
        distance = calculate_distance(edge_A, edge)
        if distance < min_distance:
            min_distance = distance
            corresponding_edge = edge_A
    
    return corresponding_edge

def calculate_length(edge_A, edge_B):
    # Calculate the length of the cut
    length = calculate_distance(edge_A, edge_B)
    return length

def calculate_distance(edge1, edge2):
    # Calculate the distance between two edges
    x1, y1 = edge1
    x2, y2 = edge2
    return ((x1-x2)**2 + (y1-y2)**2)**0.5

