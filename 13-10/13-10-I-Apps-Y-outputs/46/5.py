
def find_max_mod(x, y, n):
    for k in range(n+1):
        if k % x == y:
            return k
    return -1

def main():
    t = int(input())
    for _ in range(t):
        x, y, n = map(int, input().split())
        print(find_max_mod(x, y, n))

if __name__ == '__main__':
    main()

