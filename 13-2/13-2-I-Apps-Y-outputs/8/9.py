
def is_round(n):
    return n % 10 == 0 and all(int(d) == 0 for d in str(n)[1:])

def get_min_summands(n):
    k = 1
    while n > 0:
        if is_round(n):
            return k
        n -= 1
        k += 1
    return k

def get_summands(n):
    k = get_min_summands(n)
    result = []
    while n > 0:
        if is_round(n):
            result.append(n)
            return result
        n -= 1
    return result

def solve(n):
    k = get_min_summands(n)
    result = get_summands(n)
    return f"{k}\n{' '.join(str(r) for r in result)}"

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(solve(n))

