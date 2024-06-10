
def solve(b, d, c, l):
    # Find all possible combinations of b, d, and c that add up to l
    for i in range(1, l+1):
        for j in range(1, l+1):
            for k in range(1, l+1):
                if i + j + k == l and i >= b and j >= d and k >= c:
                    yield (i, j, k)

def main():
    b, d, c, l = map(int, input().split())
    for solution in solve(b, d, c, l):
        print(*solution)

if __name__ == '__main__':
    main()

