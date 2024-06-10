
def get_good_arrangement(r, c, a, b, c):
    # Initialize a 2D array to store the arrangement
    arrangement = [[0] * c for _ in range(r)]
    
    # Fill the first row with A bonbons
    for i in range(c):
        if a > 0:
            arrangement[0][i] = 'A'
            a -= 1
        else:
            break
    
    # Fill the remaining rows
    for i in range(1, r):
        # Fill the first column with B bonbons
        for j in range(c):
            if b > 0:
                arrangement[i][j] = 'B'
                b -= 1
            else:
                break
        
        # Fill the remaining columns
        for j in range(1, c):
            if arrangement[i][j-1] == 'A':
                arrangement[i][j] = 'B'
                b -= 1
            elif arrangement[i][j-1] == 'B':
                arrangement[i][j] = 'C'
                c -= 1
            else:
                arrangement[i][j] = 'A'
                a -= 1
    
    # Check if the arrangement is valid
    for i in range(r):
        for j in range(1, c):
            if arrangement[i][j] == arrangement[i][j-1]:
                return "impossible"
    
    # Return the valid arrangement
    return ["".join(arrangement[i]) for i in range(r)]

def main():
    r, c, a, b, c = map(int, input().split())
    arrangement = get_good_arrangement(r, c, a, b, c)
    if arrangement == "impossible":
        print("impossible")
    else:
        for row in arrangement:
            print(row)

if __name__ == '__main__':
    main()

