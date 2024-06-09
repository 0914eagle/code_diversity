
def get_input():
    n, m = map(int, input().split())
    y1 = list(map(int, input().split()))
    y2 = list(map(int, input().split()))
    return n, m, y1, y2

def get_destructible_spaceships(n, m, y1, y2):
    destructible_spaceships = 0
    for i in range(n):
        for j in range(m):
            if abs(y1[i] - y2[j]) <= 10000:
                destructible_spaceships += 1
    return destructible_spaceships

def main():
    n, m, y1, y2 = get_input()
    print(get_destructible_spaceships(n, m, y1, y2))

if __name__ == '__main__':
    main()

