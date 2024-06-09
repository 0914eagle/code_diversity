
def get_input():
    return list(map(int, input().split()))

def solve(a, b, c, d):
    max_val = 0
    for x in range(a, b+1):
        for y in range(c, d+1):
            max_val = max(max_val, x*y)
    return max_val

if __name__ == '__main__':
    a, b, c, d = get_input()
    print(solve(a, b, c, d))

