
def get_max_logo_area(picture, r1, c1, r2, c2):
    # Initialize the maximum area of the logo to 0
    max_area = 0

    # Loop through the rows of the sub-rectangle
    for i in range(r1, r2 + 1):
        # Loop through the columns of the sub-rectangle
        for j in range(c1, c2 + 1):
            # Check if the current cell is part of a Nanosoft logo
            if is_logo_cell(picture, i, j):
                # Calculate the area of the logo
                area = (r2 - r1 + 1) * (c2 - c1 + 1)

                # Update the maximum area if necessary
                max_area = max(max_area, area)

    # Return the maximum area of the logo
    return max_area

def is_logo_cell(picture, i, j):
    # Check if the current cell is part of a Nanosoft logo
    if picture[i][j] == "R" and (picture[i - 1][j] == "G" or picture[i + 1][j] == "G" or picture[i][j - 1] == "G" or picture[i][j + 1] == "G"):
        return True
    elif picture[i][j] == "G" and (picture[i - 1][j] == "R" or picture[i + 1][j] == "R" or picture[i][j - 1] == "R" or picture[i][j + 1] == "R"):
        return True
    elif picture[i][j] == "Y" and (picture[i - 1][j] == "B" or picture[i + 1][j] == "B" or picture[i][j - 1] == "B" or picture[i][j + 1] == "B"):
        return True
    elif picture[i][j] == "B" and (picture[i - 1][j] == "Y" or picture[i + 1][j] == "Y" or picture[i][j - 1] == "Y" or picture[i][j + 1] == "Y"):
        return True
    else:
        return False

def main():
    # Read the input
    n, m, q = map(int, input().split())
    picture = [input() for _ in range(n)]
    options = [tuple(map(int, input().split())) for _ in range(q)]

    # Loop through the options
    for r1, c1, r2, c2 in options:
        # Call the function to get the maximum area of the logo
        max_area = get_max_logo_area(picture, r1, c1, r2, c2)

        # Print the maximum area of the logo
        print(max_area)

if __name__ == "__main__":
    main()

