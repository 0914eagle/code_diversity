
def get_towers(brick_widths):
    towers = 0
    current_tower_height = 0
    for brick_width in brick_widths:
        if brick_width > current_tower_height:
            current_tower_height = brick_width
            towers += 1
    return towers

def main():
    num_bricks = int(input())
    brick_widths = list(map(int, input().split()))
    print(get_towers(brick_widths))

if __name__ == '__main__':
    main()

