
import math
import sys

def get_input():
    N = int(input())
    salaries = []
    for i in range(N):
        L, R = map(float, input().split())
        salaries.append((L, R))
    return N, salaries

def calculate_expected_payment(N, salaries):
    total_payment = 0
    for i in range(N):
        L, R = salaries[i]
        for j in range(i+1, N):
            Lj, Rj = salaries[j]
            total_payment += max(0, Lj - R) + max(0, L - Lj)
    return total_payment / N ** 2

def main():
    N, salaries = get_input()
    print(calculate_expected_payment(N, salaries))

if __name__ == '__main__':
    main()

