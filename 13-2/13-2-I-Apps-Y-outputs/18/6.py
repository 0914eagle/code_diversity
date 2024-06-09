
def solve(n, m, x, y, x_coords, y_coords):
    # Check if X < Z <= Y
    for z in range(x, y+1):
        # Check if x_coords < Z
        if all(x < z for x in x_coords):
            # Check if y_coords >= Z
            if all(y >= z for y in y_coords):
                return "No War"
    return "War"

