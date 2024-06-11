def minPath(grid, k):
    
    n = len(grid)
    dp = [[float('inf')] * n for _ in range(n)]
    dp[0][0] = grid[0][0]
    for i in range(n):
        for j in range(n):
            if i == 0 and j == 0:
                continue
            if i > 0:
                dp[i][j] = min(dp[i][j], dp[i-1][j] + grid[i][j])
            if j > 0:
                dp[i][j] = min(dp[i][j], dp[i][j-1] + grid[i][j])
    if dp[-1][-1] > k:
        return []
    res = []
    i, j = n-1, n-1
    while i > 0 or j > 0:
        if i > 0 and dp[i-1][j] + grid[i][j] == dp[i][j]:
            res.append(grid[i][j])
            i -= 1
        else:
            res.append(grid[i][j])
            j -= 1
    res.append(grid[0][0])
    return res[::-1]

if __name__ == '__main__':
    grid = [ [1,2,3], [4,5,6], [7,8,9]]
    k = 3
    print(minPath(grid, k))/leetcode/python/139_word_break.py
"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words,
determine if s can be segmented into a space-separated sequence