
import sys
import math

def calculate_expected_attempts(passwords):
    total_probability = sum(password[1] for password in passwords)
    expected_attempts = 0
    for i, password in enumerate(passwords):
        expected_attempts += password[1] / total_probability * (i + 1)
    return expected_attempts

def main():
    num_passwords = int(input())
    passwords = []
    for _ in range(num_passwords):
        password, probability = input().split()
        passwords.append((password, float(probability)))
    print(calculate_expected_attempts(passwords))

if __name__ == '__main__':
    main()

