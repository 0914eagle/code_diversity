
def get_max_moves(heights):
    max_moves = 0
    for i in range(len(heights)):
        current_height = heights[i]
        for j in range(i+1, len(heights)):
            if heights[j] <= current_height:
                max_moves = max(max_moves, j-i)
                break
    return max_moves

def main():
    num_squares = int(input())
    heights = list(map(int, input().split()))
    print(get_max_moves(heights))

if __name__ == '__main__':
    main()

