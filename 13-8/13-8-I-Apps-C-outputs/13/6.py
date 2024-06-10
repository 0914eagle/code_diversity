
def is_handsome(n):
    n_str = str(n)
    for i in range(len(n_str) - 1):
        if n_str[i] == n_str[i + 1]:
            return False
    return True

def get_closest_handsome_numbers(n):
    n_str = str(n)
    left, right = n_str[:-1], n_str[1:]
    left_handsome = int(left) if is_handsome(int(left)) else None
    right_handsome = int(right) if is_handsome(int(right)) else None
    if left_handsome and right_handsome:
        return left_handsome, right_handsome
    elif left_handsome:
        return left_handsome, None
    elif right_handsome:
        return right_handsome, None
    else:
        return None, None

def main():
    n = int(input())
    left, right = get_closest_handsome_numbers(n)
    if left and right:
        print(left, right)
    elif left:
        print(left)
    else:
        print(-1)

if __name__ == '__main__':
    main()

