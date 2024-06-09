
def get_min_height(heights):
    # Sort the heights in non-decreasing order
    sorted_heights = sorted(heights)
    # Initialize the minimum height to be the maximum height in the list
    min_height = sorted_heights[-1]
    # Iterate through the sorted heights and find the minimum height that satisfies the condition
    for i in range(len(sorted_heights) - 1):
        if sorted_heights[i] != sorted_heights[i + 1]:
            min_height = sorted_heights[i]
            break
    return min_height

def solve(n, m, heights):
    answers = []
    for i in range(n):
        answers.append([])
        for j in range(m):
            answers[i].append(get_min_height(heights[i][j]))
    return answers

if __name__ == '__main__':
    n, m = map(int, input().split())
    heights = []
    for i in range(n):
        heights.append(list(map(int, input().split())))
    answers = solve(n, m, heights)
    for answer in answers:
        print(*answer)

