
def is_good_matrix(matrix):
    # Check if the matrix is good
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for k in range(i, len(matrix)):
                for l in range(j, len(matrix[0])):
                    if matrix[k][l] == 1:
                        break
                else:
                    break
            else:
                break
        else:
            break
    else:
        return True
    return False

def min_changes_to_make_good(matrix):
    # Initialize variables
    changes = 0
    rows, cols = len(matrix), len(matrix[0])

    # Iterate over the matrix and check if each sub-matrix is good
    for i in range(rows):
        for j in range(cols):
            for k in range(i, rows):
                for l in range(j, cols):
                    if matrix[k][l] == 1:
                        break
                else:
                    break
            else:
                break
        else:
            continue

        # If the sub-matrix is not good, change the value of the cell at (i, j) to 1 and increment the number of changes
        matrix[i][j] = 1
        changes += 1

    return changes

def main():
    # Read input from stdin
    rows, cols = map(int, input().split())
    matrix = []
    for _ in range(rows):
        matrix.append(list(map(int, input().strip())))

    # Call the required function
    result = min_changes_to_make_good(matrix)

    # Print the result
    print(result)

if __name__ == '__main__':
    main()

