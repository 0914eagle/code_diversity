
def get_min_operations(colors):
    n = len(colors)
    counts = [0] * (n + 1)
    for color in colors:
        counts[color] += 1
    max_count = max(counts)
    min_operations = 0
    for i in range(1, n + 1):
        if counts[i] == max_count:
            min_operations += (max_count - 1)
    return min_operations

def main():
    n = int(input())
    colors = list(map(int, input().split()))
    print(get_min_operations(colors))

if __name__ == '__main__':
    main()

