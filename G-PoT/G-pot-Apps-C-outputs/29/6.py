
def min_bookcase_area(N, books):
    books.sort(reverse=True)  # Sort books by height in descending order
    dp = [[float('inf')] * 301 for _ in range(N + 1)]
    dp[0][0] = 0

    for i in range(1, N + 1):
        for j in range(1, 301):
            for k in range(1, j + 1):
                dp[i][j] = min(dp[i][j], max(dp[i - 1][j - k], books[i - 1][1]) + books[i - 1][0] * k)

    min_area = float('inf')
    for j in range(1, 301):
        min_area = min(min_area, dp[N][j] * j)

    return min_area

# Input processing
N = int(input())
books = []
for _ in range(N):
    h, t = map(int, input().split())
    books.append((h, t))

# Call the function and print the result
print(min_bookcase_area(N, books))
