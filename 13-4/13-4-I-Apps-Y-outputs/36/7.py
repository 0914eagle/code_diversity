
def read_input():
    return map(int, input().split())

def solve(x, a):
    if x < a:
        return 0
    else:
        return 10

if __name__ == '__main__':
    x, a = read_input()
    print(solve(x, a))

