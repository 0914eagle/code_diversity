
# Read input
N, T = map(int, input().split())
subjects = []
for _ in range(N):
    a, b, c = map(float, input().split())
    subjects.append((a, b, c))

# Function to calculate grade for a subject with t hours of studying
def calculate_grade(a, b, c, t):
    return a * t**2 + b * t + c

# Binary search to find the optimal time allocation for a subject
def binary_search(a, b, c):
    left, right = 0, T
    while right - left > 1e-9:
        mid = (left + right) / 2
        if calculate_grade(a, b, c, mid) <= 100:
            left = mid
        else:
            right = mid
    return left

# Calculate the maximum average grade over all subjects
def calculate_max_average_grade():
    total_grade = 0
    for a, b, c in subjects:
        optimal_time = binary_search(a, b, c)
        total_grade += calculate_grade(a, b, c, optimal_time)
    return total_grade / N

# Output the result
print("{:.10f}".format(calculate_max_average_grade()))
