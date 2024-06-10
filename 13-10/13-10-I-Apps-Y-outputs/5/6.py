
def get_input():
    N, K = map(int, input().split())
    heights = list(map(int, input().split()))
    return N, K, heights

def can_ride_rollercoaster(height, K):
    return height >= K

def count_can_ride_rollercoaster(heights, K):
    return sum(can_ride_rollercoaster(height, K) for height in heights)

def solve(N, K, heights):
    return count_can_ride_rollercoaster(heights, K)

if __name__ == '__main__':
    N, K, heights = get_input()
    print(solve(N, K, heights))

