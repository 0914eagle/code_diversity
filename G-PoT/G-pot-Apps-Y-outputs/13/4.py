
# Read input
N, M, C = map(int, input().split())
B = list(map(int, input().split()))

# Initialize counter for correct codes
correct_count = 0

# Iterate through each code
for _ in range(N):
    A = list(map(int, input().split()))
    total = sum([a * b for a, b in zip(A, B)]) + C
    if total > 0:
        correct_count += 1

# Print the number of correct codes
print(correct_count)
