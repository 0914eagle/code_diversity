
import sys
import math

def get_input():
    N = int(input())
    salaries = []
    for i in range(N):
        L, R = map(float, input().split())
        salaries.append([L, R])
    return N, salaries

def solve(N, salaries):
    expected_payment = 0
    for i in range(N):
        for j in range(i+1, N):
           Li, Ri = salaries[i]
            Lj, Rj = salaries[j]
            if Li < Lj:
                expected_payment += Lj - Li
            elif Li > Lj:
                expected_payment += Li - Lj
            if Ri < Rj:
                expected_payment += Rj - Ri
            elif Ri > Rj:
                expected_payment += Ri - Rj
    return expected_payment / (N * N)

def main():
    N, salaries = get_input()
    print(solve(N, salaries))

if __name__ == '__main__':
    main()

