
def get_min_operations(colors):
    n = len(colors)
    counts = [0] * 21
    for c in colors:
        counts[c] += 1
    counts.sort()
    max_count = counts[-1]
    min_operations = 0
    for i in range(1, 21):
        count = counts[i]
        if count > 0:
            min_operations += (count - 1) * (count - 2) // 2
    return min_operations

def main():
    n = int(input())
    colors = list(map(int, input().split()))
    print(get_min_operations(colors))

if __name__ == '__main__':
    main()

