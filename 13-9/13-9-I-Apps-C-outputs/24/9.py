
def read_input():
    n = int(input())
    c = list(map(int, input().split()))
    return n, c

def is_tree(n, c):
    if n == 1:
        return True
    if n == 2:
        return c[0] == 1 and c[1] == 1
    if n == 3:
        return c[0] == 2 and c[1] == 1 and c[2] == 1
    if n == 4:
        return c[0] == 2 and c[1] == 2 and c[2] == 1 and c[3] == 1
    if n == 5:
        return c[0] == 2 and c[1] == 3 and c[2] == 2 and c[3] == 1 and c[4] == 1
    return False

def solve():
    n, c = read_input()
    if is_tree(n, c):
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    solve()

