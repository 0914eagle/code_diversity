
def get_towers(bricks):
    towers = 0
    current_tower = 0
    for brick in bricks:
        if brick > current_tower:
            current_tower = brick
            towers += 1
    return towers

def main():
    n = int(input())
    bricks = list(map(int, input().split()))
    print(get_towers(bricks))

if __name__ == '__main__':
    main()

