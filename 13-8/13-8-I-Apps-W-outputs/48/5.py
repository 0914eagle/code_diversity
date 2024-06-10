
def read_matrix():
    n, m, d = map(int, input().split())
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().split())))
    return n, m, d, matrix

def solve(n, m, d, matrix):
    # Initialize the minimum number of moves to a large value
    min_moves = 1000
    # Loop through each element in the matrix
    for i in range(n):
        for j in range(m):
            # Check if the element is not equal to the target value
            if matrix[i][j] != d:
                # Calculate the absolute difference between the element and the target value
                abs_diff = abs(matrix[i][j] - d)
                # Check if the absolute difference is less than or equal to the minimum number of moves
                if abs_diff <= min_moves:
                    # If it is, then update the minimum number of moves
                    min_moves = abs_diff
    # Return the minimum number of moves
    return min_moves

def main():
    n, m, d, matrix = read_matrix()
    print(solve(n, m, d, matrix))

if __name__ == '__main__':
    main()

