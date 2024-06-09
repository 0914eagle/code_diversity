
def can_make_triangle(sticks):
    sticks.sort()
    for i in range(len(sticks)):
        if sticks[i] + sticks[i+1] > sticks[i+2]:
            return True
    return False

def main():
    n = int(input())
    sticks = [int(input()) for _ in range(n)]
    if can_make_triangle(sticks):
        print("possible")
    else:
        print("impossible")

if __name__ == '__main__':
    main()

