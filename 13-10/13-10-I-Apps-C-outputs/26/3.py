
def read_input():
    return map(int, input().split())

def find_tour(grid):
    # Implement your solution here
    pass

def main():
    N, M = read_input()
    grid = [[0] * M for _ in range(N)]
    tour = find_tour(grid)
    if tour is not None:
        for row, col in tour:
            print(row, col)
    else:
        print(-1)

if __name__ == '__main__':
    main()

