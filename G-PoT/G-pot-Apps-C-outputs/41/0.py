
# Read input
N, T = map(int, input().split())
subjects = []
for _ in range(N):
    a, b, c = map(float, input().split())
    subjects.append((a, b, c))

# Function to calculate grade for a subject given time
def calculate_grade(a, b, c, t):
    return a*t**2 + b*t + c

# Binary search to find optimal time allocation for a subject
def binary_search(a, b, c):
    left, right = 0, T
    while right - left > 1e-9:
        mid1 = left + (right - left) / 3
        mid2 = right - (right - left) / 3
        if calculate_grade(a, b, c, mid1) < calculate_grade(a, b, c, mid2):
            left = mid1
        else:
            right = mid2
    return calculate_grade(a, b, c, (left + right) / 2)

# Binary search to find maximum average grade
def find_max_average_grade():
    left, right = 0, 100
    for _ in range(100):
        mid1 = left + (right - left) / 3
        mid2 = right - (right - left) / 3
        total_grade = sum(binary_search(a, b, c) for a, b, c in subjects)
        total_time = sum((a * (left + right) / 2 + b) for a, b, c in subjects)
        if total_grade / total_time < total_grade / (total_time + T):
            left = mid1
        else:
            right = mid2
    return sum(binary_search(a, b, c) for a, b, c in subjects) / sum((a * (left + right) / 2 + b) for a, b, c in subjects)

# Output the result
print("{:.10f}".format(find_max_average_grade()))
