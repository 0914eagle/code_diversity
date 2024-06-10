
def read_input():
    r, c = map(int, input().split())
    image = [input() for _ in range(r)]
    return image

def get_neighbors(i, j, image):
    neighbors = []
    if i > 0 and image[i-1][j] == 'L':
        neighbors.append((i-1, j))
    if i < len(image) - 1 and image[i+1][j] == 'L':
        neighbors.append((i+1, j))
    if j > 0 and image[i][j-1] == 'L':
        neighbors.append((i, j-1))
    if j < len(image[0]) - 1 and image[i][j+1] == 'L':
        neighbors.append((i, j+1))
    return neighbors

def dfs(i, j, image, visited):
    visited.add((i, j))
    neighbors = get_neighbors(i, j, image)
    for neighbor in neighbors:
        if neighbor not in visited:
            dfs(neighbor[0], neighbor[1], image, visited)

def num_islands(image):
    visited = set()
    num_islands = 0
    for i in range(len(image)):
        for j in range(len(image[0])):
            if (i, j) not in visited and image[i][j] == 'L':
                dfs(i, j, image, visited)
                num_islands += 1
    return num_islands

def main():
    image = read_input()
    print(num_islands(image))

if __name__ == '__main__':
    main()

