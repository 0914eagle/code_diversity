
def get_towers(widths):
    towers = 0
    current_tower_width = 0
    for width in widths:
        if width > current_tower_width:
            towers += 1
            current_tower_width = width
    return towers

def main():
    num_bricks = int(input())
    widths = list(map(int, input().split()))
    print(get_towers(widths))

if __name__ == '__main__':
    main()

