
def get_max_area(picture, r1, c1, r2, c2):
    # Initialize the maximum area to 0
    max_area = 0
    
    # Loop through the sub-rectangle and check if it contains a Nanosoft logo
    for i in range(r1, r2):
        for j in range(c1, c2):
            # Check if the current cell is part of a Nanosoft logo
            if is_nanosoft_logo(picture, i, j):
                # Calculate the area of the Nanosoft logo
                area = (r2 - r1) * (c2 - c1)
                # Update the maximum area if necessary
                max_area = max(max_area, area)
    
    # Return the maximum area
    return max_area

def is_nanosoft_logo(picture, r, c):
    # Check if the current cell is part of a Nanosoft logo
    if picture[r][c] == "R" and picture[r][c+1] == "G" and picture[r+1][c] == "G" and picture[r+1][c+1] == "B":
        return True
    elif picture[r][c] == "G" and picture[r][c+1] == "R" and picture[r+1][c] == "B" and picture[r+1][c+1] == "G":
        return True
    elif picture[r][c] == "B" and picture[r][c+1] == "G" and picture[r+1][c] == "G" and picture[r+1][c+1] == "R":
        return True
    elif picture[r][c] == "Y" and picture[r][c+1] == "B" and picture[r+1][c] == "R" and picture[r+1][c+1] == "G":
        return True
    else:
        return False

def main():
    # Read the input
    n, m, q = map(int, input().split())
    picture = [input() for _ in range(n)]
    options = [input().split() for _ in range(q)]
    
    # Loop through the options and calculate the maximum area of the Nanosoft logo in each option
    for option in options:
        r1, c1, r2, c2 = map(int, option)
        print(get_max_area(picture, r1, c1, r2, c2))

if __name__ == '__main__':
    main()

