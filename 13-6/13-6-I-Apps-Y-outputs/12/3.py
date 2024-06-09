
def get_sticks_lengths(n):
    return list(map(int, input().split()))

def is_triangle(a, b, c):
    return a + b > c and b + c > a and a + c > b

def is_non_degenerate_triangle(a, b, c):
    return is_triangle(a, b, c) and a != b != c != a

def can_form_triangle(sticks):
    for i in range(len(sticks) - 2):
        for j in range(i + 1, len(sticks) - 1):
            for k in range(j + 1, len(sticks)):
                if is_non_degenerate_triangle(sticks[i], sticks[j], sticks[k]):
                    return True
    return False

def main():
    n = int(input())
    sticks = get_sticks_lengths(n)
    if can_form_triangle(sticks):
        print("possible")
    else:
        print("impossible")

if __name__ == '__main__':
    main()

