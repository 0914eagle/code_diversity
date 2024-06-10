
def read_input():
    n, m, d = map(int, input().split())
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().split())))
    return n, m, d, matrix

def solve(n, m, d, matrix):
    # Initialize the minimum number of moves to -1
    min_moves = -1
    
    # Initialize a set to keep track of the unique elements in the matrix
    unique_elements = set()
    
    # Loop through each element in the matrix
    for i in range(n):
        for j in range(m):
            # If the element is not already in the set, add it to the set
            if matrix[i][j] not in unique_elements:
                unique_elements.add(matrix[i][j])
    
    # If there is only one unique element in the matrix, return 0
    if len(unique_elements) == 1:
        return 0
    
    # Loop through each element in the matrix
    for i in range(n):
        for j in range(m):
            # If the element is not equal to the minimum element in the set, add d to the element
            if matrix[i][j] != min(unique_elements):
                matrix[i][j] += d
    
    # Return the minimum number of moves
    return min_moves

def main():
    n, m, d, matrix = read_input()
    print(solve(n, m, d, matrix))

if __name__ == '__main__':
    main()

