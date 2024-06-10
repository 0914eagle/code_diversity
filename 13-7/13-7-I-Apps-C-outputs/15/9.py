
def get_rectangles(n):
    rectangles = []
    for i in range(n):
        r1, c1, r2, c2 = map(int, input().split())
        rectangles.append((r1, c1, r2, c2))
    return rectangles

def is_nested(rect1, rect2):
    return rect1[0] <= rect2[0] and rect1[1] <= rect2[1] and rect1[2] >= rect2[2] and rect1[3] >= rect2[3]

def find_matching(rectangles):
    n = len(rectangles)
    matching = [-1] * n
    for i in range(n):
        for j in range(i+1, n):
            if is_nested(rectangles[i], rectangles[j]):
                matching[i] = j
                break
    return matching

def print_output(matching):
    for i in range(len(matching)):
        print(matching[i] + 1)

if __name__ == '__main__':
    n = int(input())
    rectangles = get_rectangles(n)
    matching = find_matching(rectangles)
    print_output(matching)

