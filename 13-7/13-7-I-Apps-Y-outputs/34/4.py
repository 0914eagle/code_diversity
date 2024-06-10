
def is_sorted(p):
    return sorted(p) == p

def can_sort(p):
    n = len(p)
    for i in range(n):
        for j in range(i+1, n):
            if p[i] > p[j]:
                return True
    return False

def main():
    n = int(input())
    p = list(map(int, input().split()))
    if is_sorted(p):
        print("YES")
    elif can_sort(p):
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()

