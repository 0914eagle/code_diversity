
def is_triangle(sticks):
    sticks.sort()
    for i in range(len(sticks)):
        if sticks[i] + sticks[i+1] > sticks[i+2]:
            return True
    return False

def main():
    n = int(input())
    sticks = list(map(int, input().split()))
    if n == 3:
        print("possible")
    elif n > 3 and is_triangle(sticks):
        print("possible")
    else:
        print("impossible")

if __name__ == '__main__':
    main()

