
def get_input():
    N = int(input())
    sticks = list(map(int, input().split()))
    return N, sticks

def is_triangle(sticks):
    sticks.sort()
    return sticks[0] + sticks[1] > sticks[2]

def main():
    N, sticks = get_input()
    if len(sticks) == 3 and is_triangle(sticks):
        print("possible")
    else:
        print("impossible")

if __name__ == '__main__':
    main()

