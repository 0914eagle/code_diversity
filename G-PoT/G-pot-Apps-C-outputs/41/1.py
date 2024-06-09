
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
        grade = a * (t ** 2) + b * t + c
        total_grade += grade
    return total_grade / N

def binary_search():
    left, right = 0, T
    eps = 1e-9
    while right - left > eps:
        mid1 = left + (right - left) / 3
        mid2 = right - (right - left) / 3
        if calculate_grade(mid1) < calculate_grade(mid2):
            left = mid1
        else:
            right = mid2
    return calculate_grade(left)

result = binary_search()
print("{:.10f}".format(result))
