
def get_min_instability(heights, k):
    # Your code here
    return s, m

def get_operations(heights, k):
    # Your code here
    return operations

if __name__ == '__main__':
    n, k = map(int, input().split())
    heights = list(map(int, input().split()))
    s, m = get_min_instability(heights, k)
    print(s, m)
    for i, j in get_operations(heights, k):
        print(i, j)

