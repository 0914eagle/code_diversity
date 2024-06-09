
def get_min_height(heights):
    # Sort the heights in non-decreasing order
    heights.sort()
    # Initialize the minimum height to be the maximum height in the list
    min_height = heights[-1]
    # Iterate through the heights and find the minimum height that is greater than or equal to each height
    for i in range(len(heights)):
        min_height = min(min_height, heights[i])
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

