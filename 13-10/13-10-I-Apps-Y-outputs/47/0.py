
import sys

def calculate_expected_attempts(passwords):
    expected_attempts = 0
    for password, probability in passwords:
        expected_attempts += probability
    return expected_attempts

def get_input():
    N = int(input())
    passwords = []
    for i in range(N):
        password, probability = input().split()
        passwords.append((password, float(probability)))
    return passwords

def main():
    passwords = get_input()
    expected_attempts = calculate_expected_attempts(passwords)
    print(f"{expected_attempts:.4f}")

if __name__ == '__main__':
    main()

