
def f1(matrix):
    # Initialize the counts for 0s, 1s, and 2s
    count_0 = 0
    count_1 = 0
    count_2 = 0

    # Loop through the matrix and count the entries
    for row in matrix:
        for entry in row:
            if entry == 0:
                count_0 += 1
            elif entry == 1:
                count_1 += 1
            elif entry == 2:
                count_2 += 1

    return count_0, count_1, count_2

def f2(matrix):
    # Initialize the counts for 0s, 1s, and 2s
    count_0 = 0
    count_1 = 0
    count_2 = 0

    # Loop through the matrix and count the entries
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            if matrix[i][j] == 0:
                count_0 += 1
            elif matrix[i][j] == 1:
                count_1 += 1
            elif matrix[i][j] == 2:
                count_2 += 1

    return count_0, count_1, count_2

if __name__ == '__main__':
    N = int(input())
    matrix = []
    for _ in range(N):
        matrix.append(list(map(int, input().split())))

    count_0, count_1, count_2 = f1(matrix)
    print(count_0, count_1, count_2)

    count_0, count_1, count_2 = f2(matrix)
    print(count_0, count_1, count_2)

