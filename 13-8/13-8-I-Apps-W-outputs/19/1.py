
def get_color_counts(colors):
    color_counts = {}
    for color in colors:
        if color not in color_counts:
            color_counts[color] = 0
        color_counts[color] += 1
    return color_counts

def get_min_operations(colors):
    color_counts = get_color_counts(colors)
    min_operations = 0
    for color, count in color_counts.items():
        min_operations += count - 1
    return min_operations

def main():
    n = int(input())
    colors = list(map(int, input().split()))
    print(get_min_operations(colors))

if __name__ == '__main__':
    main()

