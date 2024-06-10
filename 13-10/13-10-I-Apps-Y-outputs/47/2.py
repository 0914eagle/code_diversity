
import sys
import math

def get_optimal_order(passwords):
    # Sort the passwords in descending order of their probabilities
    sorted_passwords = sorted(passwords, key=lambda x: x[1], reverse=True)
    # Create a list to store the optimal order
    optimal_order = []
    # Iterate through the sorted passwords
    for password in sorted_passwords:
        # If the password is not already in the optimal order, add it
        if password not in optimal_order:
            optimal_order.append(password)
    return optimal_order

def get_expected_number_of_attempts(passwords):
    # Get the optimal order of passwords
    optimal_order = get_optimal_order(passwords)
    # Initialize the expected number of attempts to 0
    expected_attempts = 0
    # Iterate through the optimal order of passwords
    for password in optimal_order:
        # Add the probability of the current password to the expected number of attempts
        expected_attempts += password[1]
    return expected_attempts

if __name__ == '__main__':
    num_passwords = int(input())
    passwords = []
    for i in range(num_passwords):
        password, probability = input().split()
        passwords.append((password, float(probability)))
    print(get_expected_number_of_attempts(passwords))

