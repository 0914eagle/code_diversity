
def f1(N, matrix):
    # Initialize the count of 0's, 1's, and 2's
    count_0 = 0
    count_1 = 0
    count_2 = 0
    
    # Loop through the matrix and update the count
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 0:
                count_0 += 1
            elif matrix[i][j] == 1:
                count_1 += 1
            else:
                count_2 += 1
    
    # Return the count of 0's, 1's, and 2's
    return count_0, count_1, count_2

def f2(N, matrix):
    # Initialize the count of 0's, 1's, and 2's
    count_0 = 0
    count_1 = 0
    count_2 = 0
    
    # Loop through the matrix and update the count
    for i in range(N):
        for j in range(N):
            if i == 0 or j == 0:
                if matrix[i][j] == 0:
                    count_0 += 1
                elif matrix[i][j] == 1:
                    count_1 += 1
                else:
                    count_2 += 1
            else:
                if matrix[i][j] == mex(matrix[i-1][j], matrix[i][j-1]):
                    if matrix[i][j] == 0:
                        count_0 += 1
                    elif matrix[i][j] == 1:
                        count_1 += 1
                    else:
                        count_2 += 1
    
    # Return the count of 0's, 1's, and 2's
    return count_0, count_1, count_2

def mex(x, y):
    if x == 0 and y == 0:
        return 1
    elif x == 0 and y == 1:
        return 2
    elif x == 0 and y == 2:
        return 0
    elif x == 1 and y == 0:
        return 1
    elif x == 1 and y == 1:
        return 2
    elif x == 1 and y == 2:
        return 0
    elif x == 2 and y == 0:
        return 1
    elif x == 2 and y == 1:
        return 2
    elif x == 2 and y == 2:
        return 0

if __name__ == '__main__':
    N = int(input())
    matrix = []
    for i in range(N):
        matrix.append(list(map(int, input().split())))
    count_0, count_1, count_2 = f2(N, matrix)
    print(count_0, count_1, count_2)

