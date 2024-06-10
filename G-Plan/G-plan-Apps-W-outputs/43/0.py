
def calculate_time_to_authorize(n, k, passwords, target_password):
    passwords.sort(key=len)
    min_time = 1
    max_time = 1

    for i, password in enumerate(passwords):
        if password == target_password:
            min_time += i // (k + 1)
            max_time += i // (k + 1) * (k + 1)

    return min_time, max_time

if __name__ == '__main__':
    n, k = map(int, input().split())
    passwords = [input().strip() for _ in range(n)]
    target_password = input().strip()

    min_time, max_time = calculate_time_to_authorize(n, k, passwords, target_password)
    print(min_time, max_time)
