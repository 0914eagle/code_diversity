
def min_bookcase_area(N, books):
    books.sort(reverse=True)  # Sort books by height in descending order
    dp = [[float('inf')] * (N + 1) for _ in range(N + 1)]
    dp[0][0] = 0
    
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            for k in range(i):
                dp[i][j] = min(dp[i][j], max(dp[k][j - 1], sum(books[k:i]) * max(book[1] for book in books[k:i])))
    
    return dp[N][3]

# Input processing
N = int(input())
books = []
for _ in range(N):
    h, t = map(int, input().split())
    books.append((h, t))

# Calculate and output the minimum area of the bookcase
print(min_bookcase_area(N, books))
