
def get_min_height(intersection_heights):
    # Sort the heights in non-decreasing order
    sorted_heights = sorted(intersection_heights)
    # Initialize the minimum height as the largest height
    min_height = sorted_heights[-1]
    # Iterate through the heights and check if they are less than the minimum height
    for height in sorted_heights[:-1]:
        if height < min_height:
            min_height = height
    return min_height

def solve(n, m, intersection_heights):
    answers = []
    for i in range(n):
        answers.append([])
        for j in range(m):
            answers[i].append(get_min_height(intersection_heights[i][j]))
    return answers

if __name__ == '__main__':
    n, m = map(int, input().split())
    intersection_heights = []
    for i in range(n):
        intersection_heights.append(list(map(int, input().split())))
    answers = solve(n, m, intersection_heights)
    for answer in answers:
        print(*answer)

