
def f1(n):
    if n % 2 == 0:
        return "Bob"
    else:
        return "Alice"

def f2(n):
    if n == 1:
        return "Alice"
    if n == 2:
        return "Bob"
    if n % 2 == 0:
        return f2(n - 2)
    else:
        return f2(n - 1)

if __name__ == '__main__':
    n = int(input())
    print(f2(n))

