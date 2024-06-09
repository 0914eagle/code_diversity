
from typing import List

def smallest_change(arr: List[int]) -> int:
    
    n = len(arr)
    dp = [[0] * n for _ in range(n)]

    for i in range(n):
        dp[i][i] = 0

    for i in range(n-1, -1, -1):
        for j in range(i+1, n):
            if arr[i] == arr[j]:
                dp[i][j] = dp[i+1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i][j-1], dp[i+1][j], dp[i+1][j-1])

    return dp[0][n-1]

