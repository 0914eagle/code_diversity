
# Read input
N, M, K = map(int, input().split())
buildings = [0] * M
students = []
for _ in range(N):
    student_building = int(input())
    students.append(student_building)
    buildings[student_building-1] += 1

# Initialize DP table
dp = [[float('inf')] * (K+1) for _ in range(M+1)]
dp[0][0] = 0

# Dynamic Programming
for i in range(1, M+1):
    for j in range(1, K+1):
        for k in range(i):
            num_students = sum(buildings[k:i])
            dp[i][j] = min(dp[i][j], dp[k][j-1] + num_students)

# Find the minimum noise level
min_noise = min(dp[M])
print(min_noise)
