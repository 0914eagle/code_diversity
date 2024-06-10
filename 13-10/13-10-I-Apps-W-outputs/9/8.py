
def get_smallest_integer(n):
    n = str(n)
    n_len = len(n)
    for i in range(1, n_len + 1):
        if n_len % i == 0:
            if n[:i] == n[n_len - i:] and int(n[:i]) < int(n):
                return int(n[:i])
    return int(n)

def get_original_number(substring, n):
    n = str(n)
    n_len = len(n)
    for i in range(1, n_len + 1):
        if n_len % i == 0:
            if substring in n[:i] and n[:i] in n[n_len - i:] and int(n[:i]) < int(n):
                return int(n[:i])
    return int(n)

def get_smallest_initial_integer(substring):
    n = 0
    while True:
        n += 1
        if get_original_number(substring, n) == n:
            return n

if __name__ == '__main__':
    substring = input()
    print(get_smallest_initial_integer(substring))

