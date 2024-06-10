
def input_points():
    n = int(input())
    x = list(map(int, input().split()))
    return n, x

def find_subset(n, x):
    subset = []
    for i in range(n):
        subset.append(i)
    return subset

def main():
    n, x = input_points()
    subset = find_subset(n, x)
    print(len(subset))
    print(*subset)

if __name__ == '__main__':
    main()

