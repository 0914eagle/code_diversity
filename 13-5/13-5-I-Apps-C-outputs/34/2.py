
def get_min_height(intersection):
    # Sort the heights in non-decreasing order
    heights = sorted(intersection)
    # Initialize the minimum height to be the maximum height in the intersection
    min_height = heights[-1]
    # Iterate through the heights and check if they can be replaced with a smaller value
    for i in range(len(heights)):
        if heights[i] > min_height:
            min_height = heights[i]
            break
    return min_height

def solve(n, m, intersections):
    answers = []
    for i in range(n):
        answers.append([])
        for j in range(m):
            intersection = intersections[i][j]
            answers[i].append(get_min_height(intersection))
    return answers

if __name__ == '__main__':
    n, m = map(int, input().split())
    intersections = []
    for i in range(n):
        intersections.append(list(map(int, input().split())))
    answers = solve(n, m, intersections)
    for answer in answers:
        print(*answer)

