
def is_handsome(n):
    n_str = str(n)
    for i in range(len(n_str) - 1):
        if n_str[i] == n_str[i + 1]:
            return False
    return True

def find_closest_handsome_number(n):
    n_str = str(n)
    for i in range(len(n_str)):
        if n_str[i] % 2 == 0:
            n_str = n_str[:i] + '1' + n_str[i + 1:]
            break
    else:
        n_str = n_str[:-1] + '1'
    return int(n_str)

def main():
    n = int(input())
    handsome_number = find_closest_handsome_number(n)
    print(handsome_number)

if __name__ == '__main__':
    main()

