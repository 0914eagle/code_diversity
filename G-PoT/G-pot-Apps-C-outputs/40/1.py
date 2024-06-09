
def calculate_panels(n, cells):
    if n == 0:
        return 0
    
    total_panels = 6 * n  # Each cell requires 6 panels
    
    # Check for adjacent cells in the x, y, and z directions
    for cell in cells:
        x, y, z = cell
        if (x+1, y, z) in cells:
            total_panels -= 2  # Reduce panels by 2 for adjacent cells in x direction
        if (x, y+1, z) in cells:
            total_panels -= 2  # Reduce panels by 2 for adjacent cells in y direction
        if (x, y, z+1) in cells:
            total_panels -= 2  # Reduce panels by 2 for adjacent cells in z direction
    
    return total_panels

# Read input
n = int(input())
cells = []
for _ in range(n):
    x, y, z = map(int, input().split())
    cells.append((x, y, z))

# Calculate and output the minimum number of panels required
print(calculate_panels(n, cells))
