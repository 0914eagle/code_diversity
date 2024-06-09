
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

    left_str = n_str[:i] + str(int(n_str[i]) + 1) + n_str[i + 2:]
    right_str = n_str[:i] + str(int(n_str[i]) - 1) + n_str[i + 2:]
    left = int(left_str)
    right = int(right_str)

    if is_handsome(left):
        return left
    elif is_handsome(right):
        return right
    else:
        return left, right

