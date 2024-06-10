
def is_handsome(n):
    n_str = str(n)
    for i in range(len(n_str) - 1):
        if n_str[i] == n_str[i + 1]:
            return False
    return True

def get_closest_handsome_number(n):
    n_str = str(n)
    for i in range(len(n_str)):
        if n_str[i] % 2 == 0:
            n_str = n_str[:i] + '1' + n_str[i + 1:]
            break
        else:
            n_str = n_str[:i] + '0' + n_str[i + 1:]
            break
    return int(n_str)

def main():
    n = int(input())
    closest_handsome_number = get_closest_handsome_number(n)
    if is_handsome(closest_handsome_number):
        print(closest_handsome_number)
    else:
        print(closest_handsome_number, closest_handsome_number + 1)

if __name__ == '__main__':
    main()

