
def get_subset(x):
    n = len(x)
    subset = []
    for i in range(n):
        subset.append(x[i])
        for j in range(i+1, n):
            if x[j] - x[i] == 2**d for some non-negative integer d:
                subset.append(x[j])
    return subset

def main():
    n = int(input())
    x = list(map(int, input().split()))
    subset = get_subset(x)
    print(len(subset))
    print(*subset)

if __name__ == '__main__':
    main()

