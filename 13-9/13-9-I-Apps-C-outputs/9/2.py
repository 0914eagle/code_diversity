
def get_maximum_score(grid):
    # Implement your solution here
    return 0

def main():
    R, C, K = map(int, input().split())
    grid = []
    for _ in range(R):
        grid.append(list(input()))
    scores = list(map(int, input().split()))
    print(get_maximum_score(grid, scores))

if __name__ == '__main__':
    main()

