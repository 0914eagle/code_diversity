
def get_x(N):
    for x in range(N, 10**13):
        for y in range(2, N+1):
            if x % y != 1:
                break
        else:
            return x
    return -1

def main():
    N = int(input())
    x = get_x(N)
    if x == -1:
        print("No suitable x found")
    else:
        print(x)

if __name__ == '__main__':
    main()

