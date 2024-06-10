
def is_handsome(n):
    n_str = str(n)
    for i in range(len(n_str) - 1):
        if n_str[i] == n_str[i + 1]:
            return False
    return True

def get_closest_handsome_number(n):
    n_str = str(n)
    for i in range(len(n_str) - 1):
        if n_str[i] == n_str[i + 1]:
            break
    else:
        return n

    handsome_numbers = []
    for i in range(len(n_str) - 1):
        if n_str[i] != n_str[i + 1]:
            handsome_numbers.append(int(n_str[:i] + str(9 - int(n_str[i])) + n_str[i + 1:]))
            handsome_numbers.append(int(n_str[:i] + str(int(n_str[i]) + 1) + n_str[i + 1:]))
    handsome_numbers.sort()
    return handsome_numbers[0], handsome_numbers[1]

def main():
    n = int(input())
    if is_handsome(n):
        print(-1)
    else:
        print(*get_closest_handsome_number(n))

if __name__ == '__main__':
    main()

