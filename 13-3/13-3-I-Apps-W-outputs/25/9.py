
def find_rearrangement(a):
    n = len(a)
    b = [0] * n
    for i in range(n):
        b[i] = a[i]
    b.sort()
    return b

def check_rearrangement(a, b):
    n = len(a)
    for i in range(n):
        if a[i] != b[i]:
            return False
    return True

def find_nonzero_sum(b):
    n = len(b)
    for i in range(n):
        if sum(b[:i+1]) != 0:
            return True
    return False

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        b = find_rearrangement(a)
        if check_rearrangement(a, b) and find_nonzero_sum(b):
            print("YES")
            print(" ".join(map(str, b)))
        else:
            print("NO")

if __name__ == '__main__':
    main()

