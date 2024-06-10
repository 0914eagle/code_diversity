
def is_valid_arrangement(arrangement, r, c):
    # Check if the arrangement is valid by checking if any two bonbons of the same color are adjacent to each other within a row or a column
    for i in range(r):
        for j in range(c):
            if arrangement[i][j] == arrangement[i][j+1] or arrangement[i][j] == arrangement[i+1][j]:
                return False
    return True

def get_good_arrangement(a, b, c, r, c):
    # Initialize the arrangement with the first row and column
    arrangement = [['A'] * c] * r
    arrangement[0][0] = 'B'
    arrangement[0][1] = 'C'

    # Fill in the rest of the arrangement
    for i in range(1, r):
        for j in range(1, c):
            if i % 2 == 0:
                arrangement[i][j] = 'B'
            else:
                arrangement[i][j] = 'C'

    # Check if the arrangement is valid
    if is_valid_arrangement(arrangement, r, c):
        return arrangement
    else:
        return "impossible"

def main():
    r, c = map(int, input().split())
    a, b, c = map(int, input().split())
    arrangement = get_good_arrangement(a, b, c, r, c)
    if arrangement == "impossible":
        print("impossible")
    else:
        for row in arrangement:
            print("".join(row))

if __name__ == '__main__':
    main()

