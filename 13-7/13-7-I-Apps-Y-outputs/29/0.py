
def is_similar(x, y):
    return x % 2 == y % 2 or abs(x - y) == 1

def can_partition(arr):
    n = len(arr)
    if n % 2 == 1 or any(a < 1 or a > 100 for a in arr):
        return False
    for i in range(0, n, 2):
        x, y = arr[i], arr[i + 1]
        if not is_similar(x, y):
            return False
    return True

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = [int(x) for x in input().split()]
        print("YES") if can_partition(arr) else print("NO")

if __name__ == '__main__':
    main()

