
def read_input():
    N, M = map(int, input().split())
    grid = []
    for _ in range(N):
        grid.append(input())
    return N, M, grid

def get_rating(grid):
    rating = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '$':
                rating += 1
    return rating

def main():
    N, M, grid = read_input()
    print(get_rating(grid))

if __name__ == '__main__':
    main()

