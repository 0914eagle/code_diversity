
def get_closest_handsome_number(n):
    n_str = str(n)
    for i in range(len(n_str) - 1):
        if n_str[i] == n_str[i + 1]:
            return int(n_str[:i] + str(int(n_str[i]) + 1) + n_str[i + 1:])
    return n

