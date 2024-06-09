
def f1(n, q, x_coords, y_coords, a, b):
    # Find the minimum side length of the square
    side_length = min(max(x_coords), max(y_coords)) + 1
    
    # Initialize a matrix to keep track of the houses
    matrix = [[0 for _ in range(side_length)] for _ in range(side_length)]
    
    # Populate the matrix with the houses
    for i in range(n):
        matrix[x_coords[i]][y_coords[i]] = 1
    
    # Check if the houses in the range [a, b] are all in the same row or column
    if all(matrix[i][y_coords[a]] == 1 for i in range(a, b + 1)):
        return side_length
    if all(matrix[x_coords[a]][i] == 1 for i in range(a, b + 1)):
        return side_length
    
    # If not, find the minimum side length that contains all the houses
    for i in range(a, b + 1):
        for j in range(a, b + 1):
            if matrix[x_coords[i]][y_coords[j]] == 0:
                return side_length - 1
    
    return side_length

def f2(...):
    ...

if __name__ == '__main__':
    n, q = map(int, input().split())
    x_coords = list(map(int, input().split()))
    y_coords = list(map(int, input().split()))
    for _ in range(q):
        a, b = map(int, input().split())
        print(f1(n, q, x_coords, y_coords, a, b))

