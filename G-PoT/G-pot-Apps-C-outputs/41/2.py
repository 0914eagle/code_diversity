
import numpy as np

def expected_grade(a, b, c, t):
    return a * t**2 + b * t + c

def max_average_grade(N, T, subjects):
    def objective(x):
        total_grade = 0
        for i in range(N):
            total_grade += expected_grade(subjects[i][0], subjects[i][1], subjects[i][2], x[i])
        return -total_grade / N

    x0 = np.full(N, T / N)  # Initial guess for time allocation
    bounds = [(0, T) for _ in range(N)]  # Time allocation bounds

    from scipy.optimize import minimize
    result = minimize(objective, x0, bounds=bounds)

    return -result.fun

# Read input
N, T = map(int, input().split())
subjects = []
for _ in range(N):
    a, b, c = map(float, input().split())
    subjects.append((a, b, c))

# Calculate and print the maximum average grade
print("{:.10f}".format(max_average_grade(N, T, subjects)))
