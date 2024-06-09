
def get_input():
    r, c = map(int, input().split())
    image = [input() for _ in range(r)]
    return image

def is_land(image, i, j):
    return image[i][j] == 'L'

def is_water(image, i, j):
    return image[i][j] == 'W'

def is_cloud(image, i, j):
    return image[i][j] == 'C'

def dfs(image, i, j):
    if not (0 <= i < len(image) and 0 <= j < len(image[0])):
        return 0
    if is_land(image, i, j):
        return 1 + dfs(image, i+1, j) + dfs(image, i-1, j) + dfs(image, i, j+1) + dfs(image, i, j-1)
    return 0

def count_islands(image):
    islands = 0
    for i in range(len(image)):
        for j in range(len(image[0])):
            if is_land(image, i, j):
                islands += 1
    return islands

def main():
    image = get_input()
    islands = count_islands(image)
    print(islands)

if __name__ == '__main__':
    main()

