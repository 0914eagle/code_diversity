
def get_vertical_markings(n, vertical_spec):
    # Initialize the vertical markings as a 2D array of 0s
    vertical_markings = [[0] * (n+1) for _ in range(n)]
    
    # Iterate through the vertical specification and mark the appropriate borders
    for i, row in enumerate(vertical_spec):
        for j, group_size in enumerate(row):
            for k in range(group_size):
                vertical_markings[i][j+k] = 1
    
    return vertical_markings

def get_horizontal_markings(n, horizontal_spec):
    # Initialize the horizontal markings as a 2D array of 0s
    horizontal_markings = [[0] * n for _ in range(n+1)]
    
    # Iterate through the horizontal specification and mark the appropriate borders
    for i, col in enumerate(horizontal_spec):
        for j, group_size in enumerate(col):
            for k in range(group_size):
                horizontal_markings[i+k][j] = 1
    
    return horizontal_markings

def get_consistent_markings(n, vertical_spec, horizontal_spec):
    # Get the vertical markings
    vertical_markings = get_vertical_markings(n, vertical_spec)
    
    # Get the horizontal markings
    horizontal_markings = get_horizontal_markings(n, horizontal_spec)
    
    # Initialize the final markings as a 2D array of 0s
    final_markings = [[0] * (n+1) for _ in range(n)]
    
    # Combine the vertical and horizontal markings to get the final markings
    for i in range(n):
        for j in range(n+1):
            final_markings[i][j] = vertical_markings[i][j] | horizontal_markings[i][j]
    
    return final_markings

def main():
    n = int(input())
    vertical_spec = [list(map(int, input().split())) for _ in range(n)]
    horizontal_spec = [list(map(int, input().split())) for _ in range(n)]
    final_markings = get_consistent_markings(n, vertical_spec, horizontal_spec)
    for row in final_markings:
        print("".join(map(str, row)))

if __name__ == '__main__':
    main()

