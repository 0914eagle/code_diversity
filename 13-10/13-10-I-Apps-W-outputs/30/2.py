
def get_rectangles(r, c, violists):
    rectangles = []
    for i in range(1, r+1):
        for j in range(1, c+1):
            rectangles.append([i, j])
    for violist in violists:
        rectangles.remove(violist)
    return rectangles

def count_pictures(rectangles, k):
    pictures = 0
    for rectangle in rectangles:
        if rectangle[0] * rectangle[1] >= k:
            pictures += 1
    return pictures

def main():
    r, c, n, k = map(int, input().split())
    violists = []
    for i in range(n):
        x, y = map(int, input().split())
        violists.append([x, y])
    rectangles = get_rectangles(r, c, violists)
    pictures = count_pictures(rectangles, k)
    print(pictures)

if __name__ == '__main__':
    main()

