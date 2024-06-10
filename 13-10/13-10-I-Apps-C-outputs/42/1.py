
def is_good_arrangement(arrangement):
    # Check if the arrangement is valid
    for i in range(len(arrangement)):
        for j in range(len(arrangement[0])):
            if arrangement[i][j] == arrangement[i][j-1] and j > 0:
                return False
    return True

def find_good_arrangement(num_rows, num_cols, num_a, num_b, num_c):
    # Initialize the arrangement with the first row
    arrangement = [['A'] * num_cols for _ in range(num_rows)]
    
    # Fill in the rest of the arrangement
    for i in range(1, num_rows):
        for j in range(num_cols):
            if j == 0:
                if num_a > 0:
                    arrangement[i][j] = 'A'
                    num_a -= 1
                elif num_b > 0:
                    arrangement[i][j] = 'B'
                    num_b -= 1
                else:
                    arrangement[i][j] = 'C'
                    num_c -= 1
            else:
                if arrangement[i][j-1] == 'A' and num_a > 0:
                    arrangement[i][j] = 'A'
                    num_a -= 1
                elif arrangement[i][j-1] == 'B' and num_b > 0:
                    arrangement[i][j] = 'B'
                    num_b -= 1
                else:
                    arrangement[i][j] = 'C'
                    num_c -= 1
    
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

