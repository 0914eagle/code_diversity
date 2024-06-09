
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

    left_digit = n_str[i]
    right_digit = n_str[i + 1]
    if left_digit == '9' and right_digit == '9':
        return int(n_str[:i] + '8' + n_str[i + 2:])
    elif left_digit == '9':
        return int(n_str[:i] + '8' + n_str[i + 1:])
    elif right_digit == '9':
        return int(n_str[:i + 1] + '8' + n_str[i + 2:])
    else:
        return int(n_str[:i] + '9' + n_str[i + 1:])

def solve(n):
    if is_handsome(n):
        return -1
    handsome_number = get_closest_handsome_number(n)
    if handsome_number == n:
        return -1
    return handsome_number

