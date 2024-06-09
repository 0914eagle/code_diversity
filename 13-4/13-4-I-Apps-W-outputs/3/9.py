
def get_rooted_dead_bush(n):
    # Initialize the RDB with a single vertex
    rdb = [0]
    
    # Construct the RDB by adding vertices and edges
    for i in range(n-1):
        # Add a new vertex for each existing vertex that has no children
        for j in range(len(rdb)):
            if rdb[j] == 0:
                rdb.append(0)
        
        # Add edges for each existing vertex that has one child
        for j in range(len(rdb)):
            if rdb[j] == 1:
                rdb.append(0)
                rdb.append(0)
        
        # Skip vertices with more than one child
    
    return rdb

def get_claw(rdb):
    # Find the center vertex with label 1
    center = rdb.index(1)
    
    # Find the children of the center vertex
    children = []
    for i in range(len(rdb)):
        if rdb[i] == center:
            children.append(i)
    
    # Find the vertices that are children of the center vertex and have label 0
    claw = []
    for i in children:
        if rdb[i] == 0:
            claw.append(i)
    
    return claw

def get_yellow_vertices(rdb):
    # Get the claw in the RDB
    claw = get_claw(rdb)
    
    # Count the number of yellow vertices
    yellow_vertices = 0
    for i in claw:
        if rdb[i] == 1:
            yellow_vertices += 1
    
    return yellow_vertices

def main():
    # Read the input
    t = int(input())
    for i in range(t):
        n = int(input())
        
        # Get the RDB of level n
        rdb = get_rooted_dead_bush(n)
        
        # Get the maximum number of yellow vertices
        yellow_vertices = get_yellow_vertices(rdb)
        
        # Print the answer modulo 10^9 + 7
        print(yellow_vertices % (10**9 + 7))

if __name__ == '__main__':
    main()

