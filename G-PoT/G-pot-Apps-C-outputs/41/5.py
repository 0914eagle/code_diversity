
# Read input
N, T = map(int, input().split())
parameters = []
for _ in range(N):
    a, b, c = map(float, input().split())
    parameters.append((a, b, c))

# Function to calculate grade for a subject given time t
def calculate_grade(a, b, c, t):
    return a * t**2 + b * t + c

# Binary search to find optimal time allocation for each subject
def binary_search(a, b, c):
    left, right = 0, T
    while right - left > 1e-9:
        mid1 = left + (right - left) / 3
        mid2 = right - (right - left) / 3
        if calculate_grade(a, b, c, mid1) < calculate_grade(a, b, c, mid2):
            left = mid1
        else:
            right = mid2
    return (left + right) / 2

# Calculate maximum average grade
total_grade = 0
for a, b, c in parameters:
    optimal_time = binary_search(a, b, c)
    total_grade += calculate_grade(a, b, c, optimal_time)

average_grade = total_grade / N
print("{:.10f}".format(average_grade))
