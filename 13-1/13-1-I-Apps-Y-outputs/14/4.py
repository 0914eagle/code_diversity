
def find_factors(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return True, i, n//i
    return False, None, None

def solve(n):
    if find_factors(n)[0]:
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(solve(n))

