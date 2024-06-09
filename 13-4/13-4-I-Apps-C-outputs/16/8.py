
def f1(matrix):
    # Initialize the count of 0's, 1's, and 2's
    count_0 = 0
    count_1 = 0
    count_2 = 0

    # Loop through the matrix and update the count
    for row in matrix:
        for elem in row:
            if elem == 0:
                count_0 += 1
            elif elem == 1:
                count_1 += 1
            else:
                count_2 += 1

    return count_0, count_1, count_2

def f2(matrix):
    # Initialize the count of 0's, 1's, and 2's
    count_0 = 0
    count_1 = 0
    count_2 = 0

    # Loop through the matrix and update the count
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                count_0 += 1
            elif matrix[i][j] == 1:
                count_1 += 1
            else:
                count_2 += 1

    return count_0, count_1, count_2

if __name__ == '__main__':
    N = int(input())
    matrix = []
    for _ in range(N):
        matrix.append(list(map(int, input().split())))
    count_0, count_1, count_2 = f1(matrix)
    print(count_0, count_1, count_2)

