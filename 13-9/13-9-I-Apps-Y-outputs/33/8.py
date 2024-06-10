
def read_input():
    N = int(input())
    heights = list(map(int, input().split()))
    return N, heights

def move(heights):
    max_moves = 0
    for i in range(len(heights) - 1):
        if heights[i] >= heights[i + 1]:
            break
        max_moves += 1
    return max_moves

def main():
    N, heights = read_input()
    print(move(heights))

if __name__ == '__main__':
    main()

