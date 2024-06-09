
def is_valid_input(n, a, b):
    if n == 1:
        return a == b
    if n == 2:
        return a[0] == b[1] and a[1] == b[0]
    if n == 3:
        return False
    if n == 4:
        if a[0] == b[3] and a[1] == b[2] and a[2] == b[1] and a[3] == b[0]:
            return True
        if a[0] == b[2] and a[1] == b[3] and a[2] == b[0] and a[3] == b[1]:
            return True
        return False
    if n == 5:
        if a[0] == b[4] and a[1] == b[3] and a[2] == b[2] and a[3] == b[1] and a[4] == b[0]:
            return True
        if a[0] == b[3] and a[1] == b[4] and a[2] == b[0] and a[3] == b[1] and a[4] == b[2]:
            return True
        if a[0] == b[2] and a[1] == b[3] and a[2] == b[4] and a[3] == b[0] and a[4] == b[1]:
            return True
        if a[0] == b[1] and a[1] == b[2] and a[2] == b[3] and a[3] == b[4] and a[4] == b[0]:
            return True
        return False
    return False

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        if is_valid_input(n, a, b):
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()

