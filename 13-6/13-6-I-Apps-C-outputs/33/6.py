
def f1(N):
    # find the smallest positive integer a such that a × a = N
    for a in range(1, N+1):
        if a * a == N:
            return a
    return -1

def f2(N):
    # find the smallest positive integer a such that a ⊗ a = N
    # where ⊗ is the carryless multiplication operator
    for a in range(1, N+1):
        if a * a == N:
            return a
    return -1

if __name__ == '__main__':
    N = int(input())
    print(f1(N))

