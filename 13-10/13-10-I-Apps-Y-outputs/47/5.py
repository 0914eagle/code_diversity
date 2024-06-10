
def expected_attempts(passwords):
    # Initialize variables
    total_attempts = 0
    total_probability = 0

    # Iterate through the passwords and calculate the expected attempts
    for password, probability in passwords:
        total_attempts += 1 / probability
        total_probability += probability

    # Return the expected number of attempts
    return total_attempts

def main():
    # Read the number of passwords
    num_passwords = int(input())

    # Read the passwords and their probabilities
    passwords = []
    for _ in range(num_passwords):
        password, probability = input().split()
        passwords.append((password, float(probability)))

    # Calculate the expected number of attempts
    expected_attempts = expected_attempts(passwords)

    # Print the result
    print(expected_attempts)

if __name__ == '__main__':
    main()

