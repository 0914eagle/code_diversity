
def get_min_snacks(guests):
    return guests * (guests + 1) // 2

def solve(a, b):
    return min(get_min_snacks(a), get_min_snacks(b))

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(solve(a, b))

