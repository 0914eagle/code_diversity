
def read_input():
    r, c = map(int, input().split())
    image = [input() for _ in range(r)]
    return image

def is_land(image, i, j):
    return image[i][j] == 'L'

def is_water(image, i, j):
    return image[i][j] == 'W'

def is_cloud(image, i, j):
    return image[i][j] == 'C'

def is_island(image, i, j):
    if not is_land(image, i, j):
        return False
    queue = [(i, j)]
    visited = set()
    while queue:
        i, j = queue.pop(0)
        if (i, j) in visited:
            continue
        visited.add((i, j))
        for ii, jj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if 0 <= ii < len(image) and 0 <= jj < len(image[0]) and is_land(image, ii, jj):
                queue.append((ii, jj))
    return len(visited) > 1

def num_islands(image):
    num_islands = 0
    for i in range(len(image)):
        for j in range(len(image[0])):
            if is_island(image, i, j):
                num_islands += 1
    return num_islands

def main():
    image = read_input()
    print(num_islands(image))

if __name__ == '__main__':
    main()

