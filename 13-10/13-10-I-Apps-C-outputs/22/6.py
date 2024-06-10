
def f_base(n, B):
    if n == 0:
        return 0
    else:
        return (n % B) * (f_base(n // B, B) + 1)

def solve(B, N):
    if N == 0:
        return 0
    else:
        for i in range(1, N):
            if f_base(i, B) == N:
                return i
        return "impossible"

if __name__ == '__main__':
    B, N = map(int, input().split())
    print(solve(B, N))

