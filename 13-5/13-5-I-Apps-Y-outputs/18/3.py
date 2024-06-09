
def get_input():
    r, c = map(int, input().split())
    image = [input() for _ in range(r)]
    return image

def is_island(image, i, j):
    if image[i][j] == 'L':
        return True
    return False

def dfs(image, i, j):
    if not (0 <= i < len(image)) or not (0 <= j < len(image[0])):
        return 0
    if image[i][j] == 'W' or image[i][j] == 'C':
        return 0
    if image[i][j] == 'L':
        image[i][j] = 'V'
        dfs(image, i-1, j)
        dfs(image, i+1, j)
        dfs(image, i, j-1)
        dfs(image, i, j+1)
        return 1
    return 0

def count_islands(image):
    count = 0
    for i in range(len(image)):
        for j in range(len(image[0])):
            if image[i][j] == 'L' and dfs(image, i, j) == 1:
                count += 1
    return count

def main():
    image = get_input()
    print(count_islands(image))

if __name__ == '__main__':
    main()

