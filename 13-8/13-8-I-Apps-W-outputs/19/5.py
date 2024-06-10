
def get_min_operations(colors):
    n = len(colors)
    colors = sorted(colors)
    count = 0
    for i in range(n-1):
        if colors[i] == colors[i+1]:
            continue
        else:
            count += 1
    return count

def main():
    n = int(input())
    colors = list(map(int, input().split()))
    print(get_min_operations(colors))

if __name__ == '__main__':
    main()

