
def read_input():
    n, m = map(int, input().split())
    y1 = [int(x) for x in input().split()]
    y2 = [int(x) for x in input().split()]
    return n, m, y1, y2

def get_max_destroyed(n, m, y1, y2):
    destroyed = 0
    for i in range(n):
        for j in range(m):
            if abs(y1[i] - y2[j]) <= 1:
                destroyed += 1
    return destroyed

def main():
    n, m, y1, y2 = read_input()
    print(get_max_destroyed(n, m, y1, y2))

if __name__ == '__main__':
    main()

