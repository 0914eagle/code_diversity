
def min_bookcase_area(N, books):
    books.sort(reverse=True)  # Sort books by height in descending order
    dp = [[float('inf')] * 61 for _ in range(N + 1)]
    dp[0][0] = 0

    for i in range(1, N + 1):
        h, t = books[i - 1]
        for j in range(1, 61):
            for k in range(1, j + 1):
                dp[i][j] = min(dp[i][j], max(dp[i - 1][j - k], h) * max(sum(books[i - 1][1] for i in range(k)), t))

    return dp[N][60]

# Input processing
N = int(input())
books = [list(map(int, input().split())) for _ in range(N)]

# Call the function and print the result
print(min_bookcase_area(N, books))
