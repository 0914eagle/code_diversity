
def f1(N, matrix):
    # Initialize the count of 0's, 1's, and 2's
    count_0 = 0
    count_1 = 0
    count_2 = 0
    
    # Loop through the matrix and count the number of each value
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 0:
                count_0 += 1
            elif matrix[i][j] == 1:
                count_1 += 1
            else:
                count_2 += 1
    
    # Return the count of each value
    return count_0, count_1, count_2

def f2(N, matrix):
    # Initialize the count of 0's, 1's, and 2's
    count_0 = 0
    count_1 = 0
    count_2 = 0
    
    # Loop through the matrix and count the number of each value
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 0:
                count_0 += 1
            elif matrix[i][j] == 1:
                count_1 += 1
            else:
                count_2 += 1
    
    # Return the count of each value
    return count_0, count_1, count_2

if __name__ == '__main__':
    N = int(input())
    matrix = []
    for i in range(N):
        matrix.append(list(map(int, input().split())))
    count_0, count_1, count_2 = f1(N, matrix)
    print(count_0, count_1, count_2)

