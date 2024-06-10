
def get_divisible_number(l, r, d):
    # Find the smallest number greater than or equal to l that is divisible by d
    l = l + (d - (l - 1) % d)
    # If the number is still within the range, return it
    if l <= r:
        return l
    # Otherwise, find the next number after r that is divisible by d
    r = r + 1 + (d - (r - 1) % d)
    return r

def solve(queries):
    for l, r, d in queries:
        print(get_divisible_number(l, r, d))

if __name__ == '__main__':
    q = int(input())
    queries = []
    for i in range(q):
        l, r, d = map(int, input().split())
        queries.append((l, r, d))
    solve(queries)

