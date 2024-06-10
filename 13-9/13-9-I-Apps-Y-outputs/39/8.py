
def get_input():
    return list(map(int, input().split()))

def is_multiple_of_a(x, a):
    return x % a == 0

def sum_is_congruent_to_c_modulo_b(a, b, c):
    for x in range(a, 1000000001, a):
        if x % b == c:
            return True
    return False

def main():
    a, b, c = get_input()
    if not is_multiple_of_a(c, b):
        print("NO")
    else:
        print("YES" if sum_is_congruent_to_c_modulo_b(a, b, c) else "NO")

if __name__ == '__main__':
    main()

