
def is_good_arrangement(arrangement):
    # Check if the arrangement is valid
    for i in range(len(arrangement)):
        for j in range(len(arrangement[0])):
            if arrangement[i][j] == arrangement[i][j-1] and j > 0:
                return False
    return True

def find_good_arrangement(num_rows, num_cols, num_a, num_b, num_c):
    # Initialize the arrangement with the first row
    arrangement = []
    arrangement.append([])
    for i in range(num_cols):
        if i % 3 == 0:
            arrangement[0].append('A')
        elif i % 3 == 1:
            arrangement[0].append('B')
        else:
            arrangement[0].append('C')

    # Fill in the rest of the rows
    for i in range(1, num_rows):
        arrangement.append([])
        for j in range(num_cols):
            if j % 3 == 0:
                arrangement[i].append('A')
            elif j % 3 == 1:
                arrangement[i].append('B')
            else:
                arrangement[i].append('C')

    # Check if the arrangement is valid
    if is_good_arrangement(arrangement):
        return arrangement
    else:
        return None

def main():
    num_rows, num_cols = map(int, input().split())
    num_a, num_b, num_c = map(int, input().split())
    arrangement = find_good_arrangement(num_rows, num_cols, num_a, num_b, num_c)
    if arrangement is None:
        print("impossible")
    else:
        for row in arrangement:
            print("".join(row))

if __name__ == '__main__':
    main()

