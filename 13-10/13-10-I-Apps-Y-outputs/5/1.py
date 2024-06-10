
def can_ride_roller_coaster(heights, k):
    count = 0
    for height in heights:
        if height >= k:
            count += 1
    return count

def get_input():
    n, k = map(int, input().split())
    heights = list(map(int, input().split()))
    return n, k, heights

def main():
    n, k, heights = get_input()
    count = can_ride_roller_coaster(heights, k)
    print(count)

if __name__ == '__main__':
    main()

