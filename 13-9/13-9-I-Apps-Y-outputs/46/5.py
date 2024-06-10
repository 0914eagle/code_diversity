
def move_books(a):
    n = len(a)
    count = 0
    i = 0
    while i < n and a[i] == 1:
        i += 1
    j = i
    while j < n and a[j] == 0:
        j += 1
    while j < n:
        if a[j] == 1:
            i = j
            while i < n and a[i] == 1:
                i += 1
            j = i
        else:
            j += 1
        count += 1
    return count

def solve(a):
    n = len(a)
    count = 0
    for i in range(n):
        if a[i] == 1:
            count += move_books(a[:i] + [0] + a[i:])
    return count

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        print(solve(a))

if __name__ == '__main__':
    main()

