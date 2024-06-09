
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
    if left_digit == "9" and right_digit == "9":
        return int(n_str[:i] + "8" + n_str[i + 2:])
    elif left_digit == "9":
        return int(n_str[:i] + "8" + n_str[i + 1:])
    elif right_digit == "9":
        return int(n_str[:i + 1] + "8" + n_str[i + 2:])
    else:
        return int(n_str[:i] + "9" + n_str[i + 1:])

def main():
    n = int(input())
    handsome_number = get_closest_handsome_number(n)
    print(handsome_number)

if __name__ == "__main__":
    main()

