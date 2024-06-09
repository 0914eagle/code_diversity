
def count_valid_colorings(n, a):
    # Initialize the number of valid colorings to 0
    num_valid_colorings = 0
    
    # Loop through each row of the grid
    for i in range(n):
        # If the row is odd, there are n hexagons in the row
        if i % 2 == 1:
            num_hexagons = n
        # If the row is even, there are n-1 hexagons in the row
        else:
            num_hexagons = n - 1
            
        # Loop through each hexagon in the row
        for j in range(num_hexagons):
            # If the current hexagon is not colored, skip it
            if a[i][j] == -1:
                continue
                
            # If the current hexagon is colored, check if it forms a loop
            if check_loop(i, j, a):
                num_valid_colorings += 1
                
    # Return the number of valid colorings
    return num_valid_colorings

def check_loop(i, j, a):
    # Initialize the number of colored edges to 0
    num_colored_edges = 0
    
    # Loop through each edge of the hexagon
    for k in range(6):
        # If the edge is colored, increment the number of colored edges
        if a[i][j] == a[(i+1)%n][(j+1)%num_hexagons]:
            num_colored_edges += 1
            
    # If the number of colored edges is equal to the number of edges in the hexagon, return True
    if num_colored_edges == 6:
        return True
    else:
        return False

n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
    
print(count_valid_colorings(n, a))

