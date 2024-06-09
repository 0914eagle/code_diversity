
def carryless_multiplication(a, b):
    result = 0
    for i in range(len(a)):
        for j in range(len(b)):
            result += a[i] * b[j]
    return result

def find_square_root(n):
    for i in range(1, n+1):
        if i * i == n:
            return i
    return -1

def main():
    n = int(input())
    root = find_square_root(n)
    if root == -1:
        print(-1)
    else:
        print(root)

if __name__ == '__main__':
    main()

