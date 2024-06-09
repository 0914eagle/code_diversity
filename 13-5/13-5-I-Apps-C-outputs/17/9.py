
def is_handsome(n):
    n_str = str(n)
    for i in range(len(n_str) - 1):
        if n_str[i] == n_str[i + 1]:
            return False
    return True

def find_closest_handsome(n):
    n_str = str(n)
    for i in range(len(n_str) - 1):
        if n_str[i] == n_str[i + 1]:
            break
    else:
        return n

    left = int(n_str[:i] + str(int(n_str[i]) + 1) + n_str[i + 1:])
    right = int(n_str[:i] + str(int(n_str[i]) - 1) + n_str[i + 1:])

    if is_handsome(left):
        return left, right
    else:
        return right, left

