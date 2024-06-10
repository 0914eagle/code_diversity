
def good_arrangement(R, C, a, b, c):
    # Initialize a 2D array to store the arrangement
    arrangement = [[0] * C for _ in range(R)]

    # Fill the first row with A bonbons
    for i in range(C):
        if a > 0:
            arrangement[0][i] = 'A'
            a -= 1
        else:
            break

    # Fill the remaining rows
    for i in range(1, R):
        for j in range(C):
            if arrangement[i - 1][j] == 'A':
                if b > 0:
                    arrangement[i][j] = 'B'
                    b -= 1
                else:
                    return False
            elif arrangement[i - 1][j] == 'B':
                if c > 0:
                    arrangement[i][j] = 'C'
                    c -= 1
                else:
                    return False
            else:
                if a > 0:
                    arrangement[i][j] = 'A'
                    a -= 1
                elif b > 0:
                    arrangement[i][j] = 'B'
                    b -= 1
                else:
                    arrangement[i][j] = 'C'
                    c -= 1

    # Check if the arrangement is valid
    for i in range(R - 1):
        for j in range(C - 1):
            if arrangement[i][j] == arrangement[i + 1][j] or arrangement[i][j + 1] == arrangement[i][j]:
                return False

    return arrangement

def main():
    R, C = map(int, input().split())
    a, b, c = map(int, input().split())
    arrangement = good_arrangement(R, C, a, b, c)
    if arrangement:
        for row in arrangement:
            print(''.join(row))
    else:
        print("impossible")

if __name__ == '__main__':
    main()

