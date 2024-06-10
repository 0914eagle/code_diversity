
def get_picture_count(orchestra, violists, k):
    picture_count = 0
    for viola in violists:
        x, y = viola
        picture_count += count_pictures(orchestra, x, y, k)
    return picture_count

def count_pictures(orchestra, x, y, k):
    picture_count = 0
    for i in range(x, len(orchestra)):
        for j in range(y, len(orchestra[0])):
            if orchestra[i][j] == '*':
                picture_count += 1
    return picture_count

def main():
    orchestra = []
    violists = []
    k = 0
    r, c, n, k = map(int, input().split())
    for i in range(n):
        x, y = map(int, input().split())
        orchestra.append(['*'] * c)
        orchestra[x][y] = '#'
        violists.append((x, y))
    print(get_picture_count(orchestra, violists, k))

if __name__ == '__main__':
    main()

