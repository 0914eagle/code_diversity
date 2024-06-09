
def get_input():
    return list(map(int, input().split()))

def solve(a, b, c, d):
    max_value = 0
    for x in range(a, b+1):
        for y in range(c, d+1):
            max_value = max(max_value, x*y)
    return max_value

if __name__ == '__main__':
    a, b, c, d = get_input()
    print(solve(a, b, c, d))

