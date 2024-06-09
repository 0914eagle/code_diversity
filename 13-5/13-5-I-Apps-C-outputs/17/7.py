
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

    left = int(n_str[:i] + n_str[i + 1])
    right = int(n_str[:i] + n_str[i] + n_str[i + 2:])
    if is_handsome(left):
        return left, right
    else:
        return right, left

n = int(input())
closest_handsome_number = get_closest_handsome_number(n)
print(*closest_handsome_number)

