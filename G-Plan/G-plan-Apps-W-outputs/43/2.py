
def min_max_time_to_authorize(n, k, passwords, correct_password):
    passwords.sort(key=len)
    min_time = 1
    max_time = 1

    for i, password in enumerate(passwords):
        if password == correct_password:
            min_time += i
            max_time += i
            break

    max_time += (k - 1) * 5

    print(min_time, max_time)


if __name__ == '__main__':
    n, k = map(int, input().split())
    passwords = [input().strip() for _ in range(n)]
    correct_password = input().strip()

    min_max_time_to_authorize(n, k, passwords, correct_password)
