
def is_handsome(n):
    n_str = str(n)
    for i in range(len(n_str) - 1):
        if n_str[i] == n_str[i + 1]:
            return False
    return True

def find_closest_handsome_number(n):
    n_str = str(n)
    for i in range(len(n_str) - 1):
        if n_str[i] != n_str[i + 1]:
            break
    else:
        return n

    if n_str[i] == '0':
        return int(n_str[:i] + '1' + n_str[i + 1:])
    elif n_str[i] == '9':
        return int(n_str[:i] + '8' + n_str[i + 1:])
    else:
        return int(n_str[:i] + str(int(n_str[i]) + 1) + n_str[i + 1:])

def solve(n):
    handsome_number = find_closest_handsome_number(n)
    if is_handsome(handsome_number):
        return str(handsome_number)
    else:
        return str(handsome_number - 1) + ' ' + str(handsome_number)

