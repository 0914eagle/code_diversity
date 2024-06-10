
def get_max_score(grid):
    # Implement your solution here
    return max_score

def main():
    R, C, K = map(int, input().split())
    grid = []
    for _ in range(R):
        grid.append(list(input()))
    score = list(map(int, input().split()))
    print(get_max_score(grid, score))

if __name__ == '__main__':
    main()

