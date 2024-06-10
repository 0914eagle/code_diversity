
def read_passwords():
    N = int(input())
    passwords = []
    for _ in range(N):
        password, probability = input().split()
        passwords.append((password, float(probability)))
    return passwords

def optimal_order(passwords):
    optimal_order = []
    while passwords:
        max_probability = max(passwords, key=lambda x: x[1])[1]
        for password in passwords:
            if password[1] == max_probability:
                optimal_order.append(password[0])
                passwords.remove(password)
                break
    return optimal_order

def expected_attempts(passwords):
    total_attempts = 0
    for password in passwords:
        total_attempts += password[1]
    return total_attempts

if __name__ == '__main__':
    passwords = read_passwords()
    optimal_order = optimal_order(passwords)
    expected_attempts = expected_attempts(optimal_order)
    print(expected_attempts)

