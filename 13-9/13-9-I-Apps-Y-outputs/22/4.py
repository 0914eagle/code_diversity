
def get_max_width(bricks):
    return max(bricks, key=lambda x: x[0])[0]

def get_max_height(bricks):
    return max(bricks, key=lambda x: x[1])[1]

def can_complete_wall(bricks, width, height):
    max_width = get_max_width(bricks)
    max_height = get_max_height(bricks)
    if max_width * max_height < width * height:
        return False
    for brick in bricks:
        if brick[0] > width or brick[1] > height:
            return False
    return True

def main():
    height, width, num_bricks = map(int, input().split())
    bricks = []
    for _ in range(num_bricks):
        bricks.append(tuple(map(int, input().split())))
    if can_complete_wall(bricks, width, height):
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()

