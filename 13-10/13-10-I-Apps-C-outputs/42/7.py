
def get_good_arrangement(R, C, a, b, c):
    # Initialize a 2D array to store the arrangement
    arrangement = [[0] * C for _ in range(R)]
    
    # Fill the first row with bonbons of the first flavor
    for i in range(C):
        if i < a:
            arrangement[0][i] = 'A'
    
    # Fill the remaining rows
    for i in range(1, R):
        # Fill the first column with bonbons of the next flavor
        for j in range(C):
            if j < b:
                arrangement[i][j] = 'B'
        
        # Fill the remaining columns
        for j in range(1, C):
            # Check if the current cell is adjacent to a cell of the same flavor
            if arrangement[i - 1][j - 1] == arrangement[i - 1][j] == arrangement[i - 1][j + 1] == arrangement[i][j - 1] == arrangement[i][j] == arrangement[i][j + 1] == arrangement[i + 1][j - 1] == arrangement[i + 1][j] == arrangement[i + 1][j + 1]:
                # If it is, then it is not a good arrangement
                return "impossible"
            else:
                # Otherwise, fill the cell with the next flavor
                if j < c:
                    arrangement[i][j] = 'C'
    
    # If we reach this point, then we have found a good arrangement
    return arrangement

def main():
    R, C, a, b, c = map(int, input().split())
    arrangement = get_good_arrangement(R, C, a, b, c)
    if arrangement == "impossible":
        print("impossible")
    else:
        for row in arrangement:
            print("".join(row))

if __name__ == '__main__':
    main()

