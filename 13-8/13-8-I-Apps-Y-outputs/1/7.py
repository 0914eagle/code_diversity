
import sys

def read_image():
    r, c = map(int, input().split())
    image = []
    for _ in range(r):
        image.append(list(input()))
    return image

def dfs(i, j, image, visited):
    if not (0 <= i < len(image)) or not (0 <= j < len(image[0])) or visited[i][j] or image[i][j] == 'C':
        return 0
    visited[i][j] = True
    return 1 + dfs(i-1, j, image, visited) + dfs(i+1, j, image, visited) + dfs(i, j-1, image, visited) + dfs(i, j+1, image, visited)

def num_islands(image):
    visited = [[False for _ in range(len(image[0]))] for _ in range(len(image))]
    count = 0
    for i in range(len(image)):
        for j in range(len(image[0])):
            if not visited[i][j] and image[i][j] == 'L':
                count += 1
                dfs(i, j, image, visited)
    return count

def main():
    image = read_image()
    print(num_islands(image))

if __name__ == '__main__':
    main()

