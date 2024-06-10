
def is_handsome(n):
    n_str = str(n)
    if len(n_str) == 1:
        return True
    for i in range(len(n_str) - 1):
        if n_str[i] == n_str[i+1]:
            return False
    return True

def get_closest_handsome_number(n):
    n_str = str(n)
    if len(n_str) == 1:
        return n
    for i in range(len(n_str) - 1):
        if n_str[i] == n_str[i+1]:
            break
    else:
        return n
    left_diff = abs(int(n_str[:i] + n_str[i+1]) - n)
    right_diff = abs(int(n_str[:i+1] + n_str[i+2]) - n)
    if left_diff < right_diff:
        return int(n_str[:i] + n_str[i+1])
    else:
        return int(n_str[:i+1] + n_str[i+2])

def main():
    n = int(input())
    print(get_closest_handsome_number(n))

if __name__ == '__main__':
    main()

