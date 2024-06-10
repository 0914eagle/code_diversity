
def get_heights(n):
    return list(map(int, input().split()))

def can_ride_coaster(k, heights):
    return sum(1 for height in heights if height >= k)

def main():
    n, k = map(int, input().split())
    heights = get_heights(n)
    print(can_ride_coaster(k, heights))

if __name__ == '__main__':
    main()

