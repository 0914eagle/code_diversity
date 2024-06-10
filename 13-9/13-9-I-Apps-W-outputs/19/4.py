
def can_divide_array(a):
    n = len(a)
    s = sum(a)
    for i in range(n):
        for j in range(i+1, n):
            if a[i] + a[j] == s - a[i] - a[j]:
                return True
    return False

def move_element(a, i, j):
    n = len(a)
    a[j] = a[i]
    a[i] = a[i-1]
    return a

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    if can_divide_array(a):
        print("YES")
    else:
        for i in range(1, n):
            for j in range(n):
                if move_element(a, i, j) and can_divide_array(a):
                    print("YES")
                    break
            if can_divide_array(a):
                break
        else:
            print("NO")

