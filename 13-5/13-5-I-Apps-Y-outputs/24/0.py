
def f1(N):
    if N % 2 == 0:
        return "Bob"
    else:
        return "Alice"

def f2(N):
    if N == 1:
        return "Alice"
    elif N == 2:
        return "Bob"
    else:
        return f2(N-2)

if __name__ == '__main__':
    N = int(input())
    print(f2(N))

