
def is_triangle(a, b, c):
    return a + b > c and b + c > a and a + c > b

def can_form_triangle(a):
    n = len(a)
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if is_triangle(a[i], a[j], a[k]):
                    return True
    return False

n = int(input())
a = list(map(int, input().split()))
print("YES") if can_form_triangle(a) else print("NO")

