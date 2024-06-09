
def read_input():
    n, m = map(int, input().split())
    floorplan = [input() for _ in range(n)]
    return n, m, floorplan

def rotate_gargoyle(gargoyle, rotation):
    if gargoyle == 'V':
        return 'H' if rotation == 90 else 'V'
    else:
        return 'V' if rotation == 90 else 'H'

def is_solvable(n, m, floorplan):
    # Check if there is a path for a beam of light to connect each gargoyle's face to another gargoyle's face
    for i in range(n):
        for j in range(m):
            if floorplan[i][j] == 'V' or floorplan[i][j] == 'H':
                # Check if there is a path to the right
                if j < m-1 and floorplan[i][j+1] == 'V' or floorplan[i][j+1] == 'H':
                    return True
                # Check if there is a path to the left
                if j > 0 and floorplan[i][j-1] == 'V' or floorplan[i][j-1] == 'H':
                    return True
                # Check if there is a path below
                if i < n-1 and floorplan[i+1][j] == 'V' or floorplan[i+1][j] == 'H':
                    return True
                # Check if there is a path above
                if i > 0 and floorplan[i-1][j] == 'V' or floorplan[i-1][j] == 'H':
                    return True
    return False

def solve_puzzle(n, m, floorplan):
    # Initialize the number of gargoyles to rotate
    num_gargoyles_to_rotate = 0
    
    # Loop through each gargoyle and check if it can be rotated
    for i in range(n):
        for j in range(m):
            if floorplan[i][j] == 'V' or floorplan[i][j] == 'H':
                # Check if the gargoyle can be rotated
                if is_solvable(n, m, floorplan):
                    # Rotate the gargoyle and increment the number of gargoyles to rotate
                    floorplan[i][j] = rotate_gargoyle(floorplan[i][j], 90)
                    num_gargoyles_to_rotate += 1
    
    # Return the number of gargoyles to rotate
    return num_gargoyles_to_rotate

if __name__ == '__main__':
    n, m, floorplan = read_input()
    print(solve_puzzle(n, m, floorplan))

