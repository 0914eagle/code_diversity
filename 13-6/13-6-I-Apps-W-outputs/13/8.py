
def find_largest_rectangle(matrix):
    # Initialize variables
    max_area = 0
    row_count = len(matrix)
    col_count = len(matrix[0])
    visited = [[False] * col_count for _ in range(row_count)]

    # Iterate over each cell in the matrix
    for i in range(row_count):
        for j in range(col_count):
            # If the current cell is not visited and is 1, find the largest rectangle
            if not visited[i][j] and matrix[i][j] == "1":
                area = find_largest_rectangle_helper(matrix, i, j, visited)
                max_area = max(max_area, area)

    return max_area

def find_largest_rectangle_helper(matrix, i, j, visited):
    # Base case: if we reach the edge of the matrix, return 0
    if i < 0 or j < 0 or i == len(matrix) or j == len(matrix[0]):
        return 0

    # If the current cell is not 1, return 0
    if matrix[i][j] == "0":
        return 0

    # If the current cell is already visited, return the area
    if visited[i][j]:
        return 1

    # Mark the current cell as visited
    visited[i][j] = True

    # Recursive calls to find the largest rectangle in all 4 directions
    area = 1 + find_largest_rectangle_helper(matrix, i-1, j, visited) + find_largest_rectangle_helper(matrix, i, j-1, visited) + find_largest_rectangle_helper(matrix, i+1, j, visited) + find_largest_rectangle_helper(matrix, i, j+1, visited)

    return area

def main():
    matrix = [
      ["1","0","1","0","0"],
      ["1","0","1","1","1"],
      ["1","1","1","1","1"],
      ["1","0","0","1","0"]
    ]
    print(find_largest_rectangle(matrix))

if __name__ == '__main__':
    main()

