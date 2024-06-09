
def get_max_area(picture, r1, c1, r2, c2):
    # Initialize the maximum area to 0
    max_area = 0
    
    # Loop through the rows and columns of the sub-rectangle
    for i in range(r1, r2+1):
        for j in range(c1, c2+1):
            # Check if the current cell is part of a Nanosoft logo
            if picture[i][j] in ["R", "G", "Y", "B"]:
                # Calculate the area of the current cell
                area = (r2-r1+1) * (c2-c1+1)
                # Update the maximum area if necessary
                max_area = max(max_area, area)
    
    # Return the maximum area
    return max_area

def main():
    # Read the input data
    n, m, q = map(int, input().split())
    picture = [input() for _ in range(n)]
    options = [tuple(map(int, input().split())) for _ in range(q)]
    
    # Loop through the options
    for r1, c1, r2, c2 in options:
        # Calculate the maximum area of the sub-square inside the sub-rectangle
        max_area = get_max_area(picture, r1, c1, r2, c2)
        # Print the maximum area
        print(max_area)

if __name__ == '__main__':
    main()

