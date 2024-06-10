
def is_valid_arrangement(arrangement, R, C):
    # Check if the arrangement is valid by checking if any two bonbons of the same color are adjacent to each other within a row or a column
    for i in range(R):
        for j in range(C):
            if arrangement[i][j] == arrangement[i][j+1] or arrangement[i][j] == arrangement[i+1][j]:
                return False
    return True

def get_good_arrangement(a, b, c, R, C):
    # Initialize the arrangement with the first row filled with A bonbons
    arrangement = []
    for i in range(R):
        arrangement.append(['A'] * C)
    arrangement[0] = ['A'] * a + ['B'] * b + ['C'] * c

    # Fill the rest of the arrangement with the remaining bonbons
    for i in range(1, R):
        for j in range(C):
            if arrangement[i-1][j] == 'A':
                arrangement[i][j] = 'B'
            elif arrangement[i-1][j] == 'B':
                arrangement[i][j] = 'C'
            else:
                arrangement[i][j] = 'A'

    # Check if the arrangement is valid
    if is_valid_arrangement(arrangement, R, C):
        return arrangement
    else:
        return None

def main():
    R, C = map(int, input().split())
    a, b, c = map(int, input().split())
    arrangement = get_good_arrangement(a, b, c, R, C)
    if arrangement is None:
        print("impossible")
    else:
        for row in arrangement:
            print("".join(row))

if __name__ == '__main__':
    main()

