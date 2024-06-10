
def get_maximum_score(grid):
    # Implement your solution here
    return max_score

def main():
    r, c, k = map(int, input().split())
    grid = []
    for _ in range(r):
        grid.append(list(input()))
    score = list(map(int, input().split()))
    max_score = get_maximum_score(grid, score)
    print(max_score)

if __name__ == '__main__':
    main()

