
def get_input():
    N = int(input())
    heights = list(map(int, input().split()))
    return N, heights

def find_max_moves(N, heights):
    max_moves = 0
    for i in range(N):
        if i == 0:
            continue
        if heights[i] <= heights[i-1]:
            max_moves += 1
    return max_moves

def main():
    N, heights = get_input()
    print(find_max_moves(N, heights))

if __name__ == '__main__':
    main()

