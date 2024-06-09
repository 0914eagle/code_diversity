
def get_average_height(heights):
    return sum(heights) / len(heights)

def get_final_height(heights, k):
    average_height = get_average_height(heights)
    final_heights = []
    for i in range(len(heights)):
        if heights[i] >= average_height + k:
            final_heights.append(heights[i])
        else:
            final_heights.append(average_height + k)
    return final_heights

def main():
    N, k = map(int, input().split())
    heights = []
    for i in range(N):
        heights.append(float(input()))
    final_heights = get_final_height(heights, k)
    print(max(final_heights))

if __name__ == '__main__':
    main()

