
def is_handsome(n):
    n_str = str(n)
    for i in range(len(n_str) - 1):
        if n_str[i] == n_str[i + 1]:
            return False
    return True

def get_closest_handsome_numbers(n):
    n_str = str(n)
    for i in range(len(n_str)):
        if n_str[i] == '0' or n_str[i] == '9':
            continue
        n1 = int(n_str[:i] + str(int(n_str[i]) - 1) + n_str[i + 1:])
        n2 = int(n_str[:i] + str(int(n_str[i]) + 1) + n_str[i + 1:])
        if is_handsome(n1) and is_handsome(n2):
            return n1, n2
    return None, None

def main():
    n = int(input())
    n1, n2 = get_closest_handsome_numbers(n)
    if n1 is None and n2 is None:
        print(-1)
    else:
        print(n1, n2)

if __name__ == '__main__':
    main()

