
def get_max_moves(heights):
    max_moves = 0
    for i in range(len(heights)):
        current_height = heights[i]
        j = i + 1
        while j < len(heights) and heights[j] <= current_height:
            j += 1
        max_moves = max(max_moves, j - i)
    return max_moves

def main():
    num_squares = int(input())
    heights = list(map(int, input().split()))
    print(get_max_moves(heights))

if __name__ == '__main__':
    main()

