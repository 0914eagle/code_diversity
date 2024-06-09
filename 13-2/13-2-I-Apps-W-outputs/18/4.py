
def can_rearrange(a, b, x):
    
    n = len(a)
    b = sorted(b)
    for i in range(n):
        if a[i] + b[i] > x:
            return False
    return True

def main():
    t = int(input())
    for _ in range(t):
        n, x = map(int, input().split())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        if can_rearrange(a, b, x):
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()

