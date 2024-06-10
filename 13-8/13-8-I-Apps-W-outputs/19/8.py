
def get_min_operations(colors):
    n = len(colors)
    counts = [0] * (n + 1)
    for color in colors:
        counts[color] += 1
    
    # Calculate the minimum number of operations
    min_operations = 0
    for i in range(1, n + 1):
        if counts[i] > 0:
            min_operations += counts[i] - 1
    
    return min_operations

def main():
    n = int(input())
    colors = list(map(int, input().split()))
    print(get_min_operations(colors))

if __name__ == '__main__':
    main()

