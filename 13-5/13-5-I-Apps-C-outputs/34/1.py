
def get_min_height(intersection):
    # Sort the heights in ascending order
    sorted_heights = sorted(intersection)
    # Initialize the minimum height as the first element
    min_height = sorted_heights[0]
    # Iterate through the heights and check if they are greater than the minimum height
    for height in sorted_heights[1:]:
        if height > min_height:
            # If a height is greater than the minimum height, update the minimum height
            min_height = height
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

