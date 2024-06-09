
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

    left = int(n_str[:i] + n_str[i + 1])
    right = int(n_str[:i + 1] + n_str[i + 2])
    if abs(left - n) < abs(right - n):
        return [left, right]
    else:
        return [right, left]

if __name__ == '__main__':
    n = int(input())
    handsome_numbers = get_closest_handsome_numbers(n)
    print(' '.join(map(str, handsome_numbers)))

