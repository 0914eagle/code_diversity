
def min_max_time_to_authorize(n, k, passwords, codehorses_password):
    sorted_passwords = sorted(passwords, key=len)
    min_time = max_time = 0
    for i, password in enumerate(sorted_passwords):
        if password == codehorses_password:
            min_time = i // (k + 1) * 5 + 1
            max_time = (i + k) // (k + 1) * 5 + 1
            break
    print(min_time, max_time)

if __name__ == '__main__':
    n, k = map(int, input().split())
    passwords = [input().strip() for _ in range(n)]
    codehorses_password = input().strip()
    min_max_time_to_authorize(n, k, passwords, codehorses_password)
