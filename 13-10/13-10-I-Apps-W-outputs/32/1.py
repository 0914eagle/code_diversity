
def get_happiness(cake):
    # Initialize variables to keep track of happiness
    row_happiness = 0
    col_happiness = 0
    
    # Loop through each row of the cake
    for i in range(len(cake)):
        # Loop through each column of the cake
        for j in range(len(cake[i])):
            # If the current cell contains a chocolate, check if it's in the same row or column as another chocolate
            if cake[i][j] == "C":
                # Check if the current cell is in the same row as another chocolate
                for k in range(len(cake[i])):
                    if k != j and cake[i][k] == "C":
                        row_happiness += 1
                # Check if the current cell is in the same column as another chocolate
                for k in range(len(cake)):
                    if k != i and cake[k][j] == "C":
                        col_happiness += 1
    
    # Return the total happiness
    return row_happiness + col_happiness

def main():
    # Read the input
    n = int(input())
    cake = []
    for i in range(n):
        cake.append(input())
    
    # Call the get_happiness function and print the result
    print(get_happiness(cake))

if __name__ == '__main__':
    main()

