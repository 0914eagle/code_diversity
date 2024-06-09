
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
    summands = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0 and is_composite(i):
            summands.append(i)
    return summands

def get_max_composite_summands(n):
    if n == 1:
        return -1
    summands = get_composite_summands(n)
    if len(summands) == 0:
        return -1
    return len(summands)

if __name__ == '__main__':
    q = int(input())
    for _ in range(q):
        n = int(input())
        print(get_max_composite_summands(n))

