
def max_rectangle_area(matrix):
    def max_rectangle_area_helper(matrix, row, col, dp):
        if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]) or matrix[row][col] == '0':
            return 0
        if dp[row][col] != -1:
            return dp[row][col]
        dp[row][col] = 1 + max_rectangle_area_helper(matrix, row - 1, col, dp) + max_rectangle_area_helper(matrix, row, col - 1, dp) - max_rectangle_area_helper(matrix, row - 1, col - 1, dp)
        return dp[row][col]
    
    dp = [[-1 for i in range(len(matrix[0]))] for j in range(len(matrix))]
    max_area = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            max_area = max(max_area, max_rectangle_area_helper(matrix, i, j, dp))
    return max_area

