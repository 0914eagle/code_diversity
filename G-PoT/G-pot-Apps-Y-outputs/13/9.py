
# Read input
N, M, C = map(int, input().split())
B = list(map(int, input().split()))

# Initialize counter for codes that solve the problem
count = 0

# Iterate through each code
for _ in range(N):
    A = list(map(int, input().split()))
    # Calculate the sum of A_i * B_i for each code
    total = sum([a * b for a, b in zip(A, B)]) + C
    # Check if the code solves the problem
    if total > 0:
        count += 1

# Print the number of codes that solve the problem
print(count)
