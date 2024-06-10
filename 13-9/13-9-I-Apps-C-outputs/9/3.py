
def get_max_score(grid, conveyor_belts):
    # Implement your solution here
    return max_score

def main():
    R, C, K = map(int, input().split())
    grid = []
    for _ in range(R):
        grid.append(list(input()))
    conveyor_belts = [int(x) for x in input().split()]
    print(get_max_score(grid, conveyor_belts))

if __name__ == '__main__':
    main()

