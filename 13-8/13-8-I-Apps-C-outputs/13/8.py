
def is_handsome(n):
    n_str = str(n)
    for i in range(len(n_str) - 1):
        if n_str[i] == n_str[i + 1]:
            return False
    return True

def get_closest_handsome_numbers(n):
    n_str = str(n)
    for i in range(len(n_str) - 1):
        if n_str[i] == n_str[i + 1]:
            break
    else:
        return [n]

    left = int(n_str[:i] + n_str[i + 1] + n_str[i + 2:])
    right = int(n_str[:i + 1] + n_str[i + 2] + n_str[i + 3:])
    if is_handsome(left):
        return [left, right]
    else:
        return [right, left]

def main():
    n = int(input())
    handsome_numbers = get_closest_handsome_numbers(n)
    print(" ".join(str(x) for x in handsome_numbers))

if __name__ == '__main__':
    main()

