
def f1(n, f):
    # Base case: if f is already idempotent, return 1
    if f(f(1)) == f(1):
        return 1
    
    # Inductive step: try applying f twice and check if it is idempotent
    k = 2
    while True:
        if f(f(f(1))) == f(f(1)):
            return k
        k += 1

def f2(n, f):
    # Base case: if f is already idempotent, return 1
    if f(f(1)) == f(1):
        return 1
    
    # Inductive step: try applying f repeatedly and check if it is idempotent
    k = 2
    while True:
        if f(f(f(f(1)))) == f(f(1)):
            return k
        k += 1

if __name__ == '__main__':
    n = int(input())
    f = list(map(int, input().split()))
    print(f1(n, f))
    print(f2(n, f))

