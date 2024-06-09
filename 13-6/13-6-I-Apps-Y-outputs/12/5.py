
def is_triangle(sticks):
    sticks.sort()
    return sticks[0] + sticks[1] > sticks[2]

def is_non_degenerate_triangle(sticks):
    return is_triangle(sticks) and sticks[0] != sticks[1] and sticks[1] != sticks[2]

def main():
    num_sticks = int(input())
    sticks = list(map(int, input().split()))
    if num_sticks == 3:
        print("possible")
    elif num_sticks == 4:
        if is_triangle(sticks):
            print("possible")
        else:
            print("impossible")
    else:
        if is_non_degenerate_triangle(sticks):
            print("possible")
        else:
            print("impossible")

if __name__ == '__main__':
    main()

