
def get_good_arrangement(r, c, a, b, c):
    # Initialize a 2D array to store the arrangement
    arrangement = [[0] * c for _ in range(r)]
    
    # Fill the first row with A bonbons
    for i in range(c):
        if a > 0:
            arrangement[0][i] = 'A'
            a -= 1
    
    # Fill the remaining rows
    for i in range(1, r):
        # Fill the first column with A bonbons
        for j in range(c):
            if a > 0:
                arrangement[i][j] = 'A'
                a -= 1
        
        # Fill the remaining columns
        for j in range(1, c):
            if arrangement[i - 1][j - 1] == 'A' and b > 0:
                arrangement[i][j] = 'B'
                b -= 1
            elif arrangement[i - 1][j - 1] == 'B' and c > 0:
                arrangement[i][j] = 'C'
                c -= 1
            else:
                return 'impossible'
    
    return arrangement

def main():
    r, c, a, b, c = map(int, input().split())
    arrangement = get_good_arrangement(r, c, a, b, c)
    if arrangement == 'impossible':
        print('impossible')
    else:
        for row in arrangement:
            print(''.join(row))

if __name__ == '__main__':
    main()

