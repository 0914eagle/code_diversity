
def is_similar(x, y):
    return x % 2 == y % 2 or abs(x - y) == 1

def has_similar_partition(a):
    n = len(a)
    if n % 2 == 1:
        return False
    for i in range(0, n - 1, 2):
        x, y = a[i], a[i + 1]
        if not is_similar(x, y):
            return False
    return True

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        print("YES") if has_similar_partition(a) else print("NO")

if __name__ == '__main__':
    main()

