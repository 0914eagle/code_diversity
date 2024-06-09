
def get_max_subsquare_area(picture, r1, c1, r2, c2):
    # Initialize the maximum area of sub-square as 0
    max_area = 0
    
    # Iterate over the sub-rectangle
    for i in range(r1, r2):
        for j in range(c1, c2):
            # Check if the current cell is the top-left cell of a sub-square
            if picture[i][j] == picture[i][j+1] == picture[i+1][j] == picture[i+1][j+1]:
                # Calculate the area of the sub-square
                area = (j - c1 + 1) * (i - r1 + 1)
                # Update the maximum area if necessary
                max_area = max(max_area, area)
    
    return max_area

def solve(n, m, q, picture, options):
    # Iterate over the options
    for i in range(q):
        # Get the coordinates of the current option
        r1, c1, r2, c2 = options[i]
        # Get the maximum area of sub-square inside the current option
        max_area = get_max_subsquare_area(picture, r1, c1, r2, c2)
        # Print the result
        print(max_area)

def main():
    # Read the input
    n, m, q = map(int, input().split())
    picture = [input() for _ in range(n)]
    options = [list(map(int, input().split())) for _ in range(q)]
    # Solve the problem
    solve(n, m, q, picture, options)

if __name__ == '__main__':
    main()

