
def get_maximum_score(grid, conveyor_belts):
    # Implement your solution here
    return 0

def main():
    R, C, K = map(int, input().split())
    grid = []
    for _ in range(R):
        grid.append(list(input()))
    conveyor_belts = []
    for _ in range(K):
        conveyor_belts.append(list(input()))
    print(get_maximum_score(grid, conveyor_belts))

if __name__ == '__main__':
    main()

