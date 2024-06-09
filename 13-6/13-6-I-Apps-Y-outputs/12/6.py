
def get_sticks_input():
    N = int(input())
    sticks = [int(i) for i in input().split()]
    return N, sticks

def is_triangle(a, b, c):
    return a + b > c and b + c > a and a + c > b

def is_non_degenerate_triangle(a, b, c):
    return is_triangle(a, b, c) and a != b != c != a

def can_make_triangle(sticks):
    for i in range(len(sticks)):
        for j in range(i+1, len(sticks)):
            for k in range(j+1, len(sticks)):
                if is_non_degenerate_triangle(sticks[i], sticks[j], sticks[k]):
                    return True
    return False

def main():
    N, sticks = get_sticks_input()
    if can_make_triangle(sticks):
        print("possible")
    else:
        print("impossible")

if __name__ == '__main__':
    main()

