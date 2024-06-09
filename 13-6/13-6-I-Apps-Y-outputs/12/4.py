
def get_stick_lengths(n):
    return list(map(int, input().split()))

def is_triangle(a, b, c):
    return a + b > c and b + c > a and a + c > b

def is_non_degenerate_triangle(a, b, c):
    return is_triangle(a, b, c) and a != b != c != a

def can_make_triangle(stick_lengths):
    for i in range(len(stick_lengths)):
        for j in range(i+1, len(stick_lengths)):
            for k in range(j+1, len(stick_lengths)):
                if is_non_degenerate_triangle(stick_lengths[i], stick_lengths[j], stick_lengths[k]):
                    return True
    return False

def main():
    n = int(input())
    stick_lengths = get_stick_lengths(n)
    if can_make_triangle(stick_lengths):
        print("possible")
    else:
        print("impossible")

if __name__ == '__main__':
    main()

