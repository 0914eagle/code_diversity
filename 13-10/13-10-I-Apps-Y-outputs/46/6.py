
def get_max_k(x, y, n):
    for k in range(n+1):
        if k%x == y:
            return k
    return -1

def main():
    t = int(input())
    for _ in range(t):
        x, y, n = map(int, input().split())
        k = get_max_k(x, y, n)
        print(k)

if __name__ == '__main__':
    main()

