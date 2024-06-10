
def get_tower_count(bricks):
    tower_count = 0
    current_tower_height = 0
    for brick in bricks:
        if brick > current_tower_height:
            tower_count += 1
            current_tower_height = brick
        else:
            current_tower_height += brick
    return tower_count

def main():
    num_bricks = int(input())
    bricks = list(map(int, input().split()))
    print(get_tower_count(bricks))

if __name__ == '__main__':
    main()

