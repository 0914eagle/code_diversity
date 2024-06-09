
def f1(matrix):
    # Initialize the count of 0's, 1's, and 2's
    count_0 = 0
    count_1 = 0
    count_2 = 0

    # Loop through the matrix and count the number of each value
    for row in matrix:
        for value in row:
            if value == 0:
                count_0 += 1
            elif value == 1:
                count_1 += 1
            else:
                count_2 += 1

    # Return the count of each value
    return count_0, count_1, count_2

def f2(matrix):
    # Initialize the count of 0's, 1's, and 2's
    count_0 = 0
    count_1 = 0
    count_2 = 0

    # Loop through the matrix and count the number of each value
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            if matrix[i][j] == 0:
                count_0 += 1
            elif matrix[i][j] == 1:
                count_1 += 1
            else:
                count_2 += 1

    # Return the count of each value
    return count_0, count_1, count_2

if __name__ == '__main__':
    # Read the input matrix
    N = int(input())
    matrix = []
    for _ in range(N):
        matrix.append(list(map(int, input().split())))

    # Call the functions to count the number of 0's, 1's, and 2's
    count_0, count_1, count_2 = f1(matrix)
    print(count_0, count_1, count_2)

    # Call the functions to count the number of 0's, 1's, and 2's
    count_0, count_1, count_2 = f2(matrix)
    print(count_0, count_1, count_2)

