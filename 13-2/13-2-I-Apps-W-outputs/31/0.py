
def max_rectangle_area(matrix):
    def dfs(i, j):
        if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]) or matrix[i][j] == '0':
            return 0
        area = dfs(i+1, j) + dfs(i-1, j) + dfs(i, j+1) + dfs(i, j-1) + 1
        return area
    
    max_area = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == '1':
                max_area = max(max_area, dfs(i, j))
    return max_area

