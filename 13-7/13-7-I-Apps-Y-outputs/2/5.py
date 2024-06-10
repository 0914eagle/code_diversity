
def is_divisible_by_25(n):
    while n % 25 != 0:
        n = swap_adjacent_digits(n)
    return n

def swap_adjacent_digits(n):
    n_str = str(n)
    n_len = len(n_str)
    for i in range(n_len - 1):
        if n_str[i] != '0' and n_str[i + 1] != '0':
            n_str = n_str[:i] + n_str[i + 1] + n_str[i] + n_str[i + 2:]
            break
    return int(n_str)

def main():
    n = int(input())
    print(is_divisible_by_25(n))

if __name__ == '__main__':
    main()

