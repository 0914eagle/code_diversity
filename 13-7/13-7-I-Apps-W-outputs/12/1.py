
def get_x(n):
    for x in range(n, 10**13):
        for y in range(2, n+1):
            if x % y != 1:
                break
        else:
            return x
    return -1

def main():
    n = int(input())
    x = get_x(n)
    if x == -1:
        print(-1)
    else:
        print(x)

if __name__ == '__main__':
    main()

