
def is_possible(n, c):
    if n == 1:
        return True
    if n == 2:
        return c[0] == c[1]
    if n == 3:
        return c[0] == c[1] and c[1] == c[2]
    if n == 4:
        return c[0] + c[1] + c[2] + c[3] == sum(c)
    return False

def solve(n, c):
    if is_possible(n, c):
        return "YES"
    return "NO"

if __name__ == '__main__':
    n = int(input())
    c = list(map(int, input().split()))
    print(solve(n, c))

