
# Read input
N, T = map(int, input().split())
subjects = []
for _ in range(N):
    a, b, c = map(float, input().split())
    subjects.append((a, b, c))

# Binary search to find the maximum average grade
def calculate_grade(t):
    total_grade = 0
    for a, b, c in subjects:
        grade = a * t**2 + b * t + c
        total_grade += grade
    return total_grade / N

low, high = 0, T
while high - low > 1e-9:
    mid1 = low + (high - low) / 3
    mid2 = high - (high - low) / 3
    if calculate_grade(mid1) < calculate_grade(mid2):
        low = mid1
    else:
        high = mid2

# Output the result with 10 decimal places
print("{:.10f}".format(calculate_grade(low)))
