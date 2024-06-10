
def get_towers(bricks):
    towers = 0
    current_tower = 0
    for brick in bricks:
        if brick > current_tower:
            towers += 1
            current_tower = brick
    return towers

def main():
    num_bricks = int(input())
    bricks = [int(x) for x in input().split()]
    print(get_towers(bricks))

if __name__ == '__main__':
    main()

