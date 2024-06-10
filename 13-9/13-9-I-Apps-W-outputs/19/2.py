
def can_divide(a):
    n = len(a)
    s = sum(a)
    for i in range(n):
        for j in range(i+1, n):
            if a[i] + a[j] == s - a[i] - a[j]:
                return True
    return False

def move_element(a, i, j):
    n = len(a)
    if i == j:
        return a
    elif i == 0:
        return a[j-1:j] + a[:j-1] + a[j:]
    elif j == n-1:
        return a[:i] + a[i+1:] + a[i:i+1]
    else:
        return a[:i] + a[j:j+1] + a[i:i+1] + a[j+1:n]

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    if can_divide(a):
        print("YES")
    else:
        for i in range(n):
            for j in range(n):
                if move_element(a, i, j) == a:
                    continue
                if can_divide(move_element(a, i, j)):
                    print("YES")
                    break
            else:
                continue
            break
        else:
            print("NO")

