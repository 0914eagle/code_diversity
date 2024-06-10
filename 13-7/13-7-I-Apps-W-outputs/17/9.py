
def get_lost_potatoes(y, k, n):
    lost_potatoes = []
    for x in range(1, n // k + 1):
        if (x + y) % k == 0 and x + y <= n:
            lost_potatoes.append(x)
    return lost_potatoes

def main():
    y, k, n = map(int, input().split())
    lost_potatoes = get_lost_potatoes(y, k, n)
    if lost_potatoes:
        print(*lost_potatoes)
    else:
        print(-1)

if __name__ == '__main__':
    main()

