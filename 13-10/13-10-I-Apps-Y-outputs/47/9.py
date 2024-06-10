
def get_probability(passwords):
    total_probability = 0
    for password, probability in passwords:
        total_probability += probability
    return total_probability

def get_expected_attempts(passwords):
    total_probability = get_probability(passwords)
    expected_attempts = 0
    for password, probability in passwords:
        expected_attempts += probability / total_probability * (passwords.index(password) + 1)
    return expected_attempts

def main():
    num_passwords = int(input())
    passwords = []
    for i in range(num_passwords):
        password, probability = input().split()
        passwords.append((password, float(probability)))
    print(get_expected_attempts(passwords))

if __name__ == '__main__':
    main()

