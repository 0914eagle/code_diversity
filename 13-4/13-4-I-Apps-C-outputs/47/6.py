
def is_handsome(n):
    n_str = str(n)
    for i in range(len(n_str) - 1):
        if n_str[i] == n_str[i + 1]:
            return False
    return True

def get_closest_handsome_numbers(n):
    n_str = str(n)
    for i in range(len(n_str)):
        if n_str[i] % 2 == 0:
            n_str = n_str[:i] + '1' + n_str[i + 1:]
            break
    else:
        n_str = n_str[:-1] + '1'
    handsome_num1 = int(n_str)

    for i in range(len(n_str)):
        if n_str[i] % 2 == 1:
            n_str = n_str[:i] + '0' + n_str[i + 1:]
            break
    else:
        n_str = n_str[:-1] + '0'
    handsome_num2 = int(n_str)

    return handsome_num1, handsome_num2

def main():
    n = int(input())
    handsome_num1, handsome_num2 = get_closest_handsome_numbers(n)
    print(handsome_num1, handsome_num2)

if __name__ == '__main__':
    main()

