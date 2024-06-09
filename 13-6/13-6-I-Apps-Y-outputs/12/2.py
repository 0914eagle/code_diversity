
def is_triangle(sticks):
    sticks.sort()
    return sticks[0] + sticks[1] > sticks[2]

def main():
    n = int(input())
    sticks = list(map(int, input().split()))
    if len(sticks) != 3:
        print("impossible")
    elif is_triangle(sticks):
        print("possible")
    else:
        print("impossible")

if __name__ == '__main__':
    main()

