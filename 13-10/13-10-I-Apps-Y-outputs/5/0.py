
def get_input():
    n, k = map(int, input().split())
    heights = list(map(int, input().split()))
    return n, k, heights

def can_ride(heights, k):
    return sum(1 for h in heights if h >= k)

def solve(n, k, heights):
    return can_ride(heights, k)

if __name__ == '__main__':
    n, k, heights = get_input()
    print(solve(n, k, heights))

