
def calculate_time(n, k, passwords, correct_password):
    passwords.sort(key=len)
    min_time = 1
    max_time = 1

    for i, password in enumerate(passwords):
        if password == correct_password:
            min_time += i // (k + 1)
            max_time += (i // k) * 5 + 1

    return min_time, max_time

if __name__ == '__main__':
    n, k = map(int, input().split())
    passwords = [input().strip() for _ in range(n)]
    correct_password = input().strip()

    min_time, max_time = calculate_time(n, k, passwords, correct_password)
    print(min_time, max_time)
