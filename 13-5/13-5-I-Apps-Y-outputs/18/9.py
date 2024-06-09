
def get_input():
    r, c = map(int, input().split())
    image = [input() for _ in range(r)]
    return image

def is_island(image, i, j):
    if image[i][j] == 'C':
        return False
    if image[i][j] == 'L':
        return True
    return False

def dfs(image, i, j):
    if not is_island(image, i, j):
        return 0
    image[i][j] = 'V'
    count = 1
    for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
        if 0 <= x < len(image) and 0 <= y < len(image[0]):
            count += dfs(image, x, y)
    return count

def solve(image):
    count = 0
    for i in range(len(image)):
        for j in range(len(image[0])):
            if is_island(image, i, j):
                count += dfs(image, i, j)
    return count

def main():
    image = get_input()
    print(solve(image))

if __name__ == '__main__':
    main()

