
import numpy as np

N, T = map(int, input().split())
grades = []
for _ in range(N):
    a, b, c = map(float, input().split())
    grades.append((a, b, c))

def calculate_grade(t, params):
    a, b, c = params
    return a*t**2 + b*t + c

def average_grade(t_allocations):
    total_grade = 0
    for i in range(N):
        total_grade += calculate_grade(t_allocations[i], grades[i])
    return total_grade / N

def objective_function(t_allocations):
    return -average_grade(t_allocations)

from scipy.optimize import minimize

initial_guess = [T/N]*N
bounds = [(0, T)]*N
result = minimize(objective_function, initial_guess, bounds=bounds)
max_avg_grade = -result.fun
print(f"{max_avg_grade:.10f}")
