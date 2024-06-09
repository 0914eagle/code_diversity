
def read_input():
    r, c = map(int, input().split())
    image = [input() for _ in range(r)]
    return r, c, image

def is_island(image, i, j):
    if image[i][j] == 'L':
        return True
    return False

def count_islands(image):
    nr, nc = len(image), len(image[0])
    count = 0
    for i in range(nr):
        for j in range(nc):
            if is_island(image, i, j):
                count += 1
    return count

def main():
    r, c, image = read_input()
    print(count_islands(image))

if __name__ == '__main__':
    main()

