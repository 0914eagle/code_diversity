
def get_input():
    r, c = map(int, input().split())
    image = [input() for _ in range(r)]
    return image

def is_land(row, col, image):
    return image[row][col] == 'L'

def is_water(row, col, image):
    return image[row][col] == 'W'

def is_cloud(row, col, image):
    return image[row][col] == 'C'

def is_connected(row1, col1, row2, col2, image):
    if is_land(row1, col1, image) and is_land(row2, col2, image):
        return True
    if is_water(row1, col1, image) and is_water(row2, col2, image):
        return True
    if is_cloud(row1, col1, image) and is_cloud(row2, col2, image):
        return True
    return False

def dfs(row, col, image, visited):
    if row < 0 or col < 0 or row >= len(image) or col >= len(image[0]):
        return
    if visited[row][col] or not is_connected(row, col, row - 1, col, image):
        return
    visited[row][col] = True
    dfs(row + 1, col, image, visited)
    dfs(row - 1, col, image, visited)
    dfs(row, col + 1, image, visited)
    dfs(row, col - 1, image, visited)

def count_islands(image):
    visited = [[False for _ in range(len(image[0]))] for _ in range(len(image))]
    count = 0
    for row in range(len(image)):
        for col in range(len(image[0])):
            if not visited[row][col] and is_land(row, col, image):
                dfs(row, col, image, visited)
                count += 1
    return count

def main():
    image = get_input()
    print(count_islands(image))

if __name__ == '__main__':
    main()

