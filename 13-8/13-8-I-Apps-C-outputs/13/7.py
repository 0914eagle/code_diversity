
def is_handsome(n):
    n_str = str(n)
    for i in range(len(n_str) - 1):
        if n_str[i] == n_str[i + 1]:
            return False
    return True

def get_closest_handsome_numbers(n):
    n_str = str(n)
    for i in range(len(n_str)):
        if n_str[i] == '9':
            n_str = n_str[:i] + '0' + n_str[i + 1:]
            break
    n1 = int(n_str)
    n2 = int(n_str) + 1
    return n1, n2

def main():
    n = int(input())
    if is_handsome(n):
        print(-1)
    else:
        n1, n2 = get_closest_handsome_numbers(n)
        print(n1, n2)

if __name__ == '__main__':
    main()

