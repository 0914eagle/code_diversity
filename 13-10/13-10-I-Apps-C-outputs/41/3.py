
import sys
import numpy as np

def get_input():
    n, m, s = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    return n, m, s, a, b, c

def find_optimal_solution(n, m, s, a, b, c):
    passes_needed = [0] * n
    for i in range(n):
        passes_needed[i] = c[i] // b[i]
        if c[i] % b[i] != 0:
            passes_needed[i] += 1
    passes_needed.sort(reverse=True)
    optimal_solution = [-1] * m
    for i in range(m):
        student_idx = np.argmax(passes_needed)
        optimal_solution[i] = student_idx
        passes_needed[student_idx] -= 1
    return optimal_solution

def print_output(solution):
    print("YES")
    for i in solution:
        print(i+1, end=" ")
    print()

def main():
    n, m, s, a, b, c = get_input()
    solution = find_optimal_solution(n, m, s, a, b, c)
    print_output(solution)

if __name__ == '__main__':
    main()

