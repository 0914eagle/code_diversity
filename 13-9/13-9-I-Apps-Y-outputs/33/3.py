
def get_input():
    n = int(input())
    heights = list(map(int, input().split()))
    return n, heights

def solve(n, heights):
    max_moves = 0
    for i in range(n):
        if heights[i] > heights[i-1]:
            continue
        moves = 1
        while i+moves < n and heights[i+moves] <= heights[i]:
            moves += 1
        max_moves = max(max_moves, moves)
    return max_moves

def main():
    n, heights = get_input()
    print(solve(n, heights))

if __name__ == '__main__':
    main()

