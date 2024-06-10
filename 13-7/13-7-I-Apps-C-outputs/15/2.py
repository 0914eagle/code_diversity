
def find_rectangles(corner_pairs):
    rectangles = []
    for i in range(len(corner_pairs)):
        top_left, bottom_right = corner_pairs[i]
        for j in range(i+1, len(corner_pairs)):
            if top_left[0] <= corner_pairs[j][0][0] <= bottom_right[0] and top_left[1] <= corner_pairs[j][0][1] <= bottom_right[1]:
                rectangles.append([i+1, j+1])
    return rectangles

def check_rectangles(rectangles):
    for i in range(len(rectangles)):
        for j in range(i+1, len(rectangles)):
            if rectangles[i][0] == rectangles[j][1] or rectangles[i][1] == rectangles[j][0]:
                return "syntax error"
    return rectangles

def main():
    corner_pairs = []
    for i in range(int(input())):
        top_left = [int(j) for j in input().split()]
        bottom_right = [int(j) for j in input().split()]
        corner_pairs.append([top_left, bottom_right])
    rectangles = find_rectangles(corner_pairs)
    result = check_rectangles(rectangles)
    if result == "syntax error":
        print(result)
    else:
        for i in range(len(result)):
            print(result[i][0], result[i][1])

if __name__ == '__main__':
    main()

