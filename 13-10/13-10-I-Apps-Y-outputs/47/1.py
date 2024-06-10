
import sys
import math

def get_input():
    N = int(input())
    passwords = []
    for i in range(N):
        password, probability = input().split()
        passwords.append((password, float(probability)))
    return N, passwords

def get_expected_attempts(N, passwords):
    expected_attempts = 0
    for i in range(N):
        for j in range(i+1, N):
            if passwords[i][1] > passwords[j][1]:
                expected_attempts += 1
    return expected_attempts / N

def main():
    N, passwords = get_input()
    expected_attempts = get_expected_attempts(N, passwords)
    print(expected_attempts)

if __name__ == '__main__':
    main()

