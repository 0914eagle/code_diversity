
def read_image(r, c):
    image = []
    for _ in range(r):
        image.append(input())
    return image

def get_neighbors(i, j, image):
    neighbors = []
    if i > 0 and image[i-1][j] == 'L':
        neighbors.append((i-1, j))
    if i < len(image)-1 and image[i+1][j] == 'L':
        neighbors.append((i+1, j))
    if j > 0 and image[i][j-1] == 'L':
        neighbors.append((i, j-1))
    if j < len(image[0])-1 and image[i][j+1] == 'L':
        neighbors.append((i, j+1))
    return neighbors

def dfs(i, j, image, visited):
    visited[i][j] = True
    neighbors = get_neighbors(i, j, image)
    for neighbor in neighbors:
        if not visited[neighbor[0]][neighbor[1]]:
            dfs(neighbor[0], neighbor[1], image, visited)

def get_islands(image):
    visited = [[False for _ in range(len(image[0]))] for _ in range(len(image))]
    islands = 0
    for i in range(len(image)):
        for j in range(len(image[0])):
            if not visited[i][j] and image[i][j] == 'L':
                dfs(i, j, image, visited)
                islands += 1
    return islands

def main():
    r, c = map(int, input().split())
    image = read_image(r, c)
    print(get_islands(image))

if __name__ == '__main__':
    main()

