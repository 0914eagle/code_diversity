
def can_make_package(n, a, b, c, d):
    if c - d < n * (a - b) or c + d > n * (a + b):
        return "No"
    return "Yes"

def main():
    t = int(input())
    for _ in range(t):
        n, a, b, c, d = map(int, input().split())
        print(can_make_package(n, a, b, c, d))

if __name__ == '__main__':
    main()

