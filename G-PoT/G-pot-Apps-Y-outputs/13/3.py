
# Read input
N, M, C = map(int, input().split())
B = list(map(int, input().split()))

# Initialize counter
count = 0

# Check each code
for _ in range(N):
    A = list(map(int, input().split()))
    if sum([a * b for a, b in zip(A, B)]) + C > 0:
        count += 1

# Print the count of correct codes
print(count)
