
def is_composite(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return True
    return False

def get_composite_summands(n):
    if n == 1:
        return []
    if is_composite(n):
        return [n]
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            return [i] + get_composite_summands(n // i)
    return []

def get_max_composite_summands(n):
    if n == 1:
        return 0
    summands = get_composite_summands(n)
    if len(summands) == 0:
        return -1
    return len(summands)

if __name__ == '__main__':
    q = int(input())
    for _ in range(q):
        n = int(input())
        print(get_max_composite_summands(n))

