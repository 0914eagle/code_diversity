
def can_ride_roller_coaster(heights, k):
    count = 0
    for height in heights:
        if height >= k:
            count += 1
    return count

def get_heights(n):
    return list(map(int, input().split()))

def get_k():
    return int(input())

def main():
    n = get_k()
    heights = get_heights(n)
    count = can_ride_roller_coaster(heights, n)
    print(count)

if __name__ == '__main__':
    main()

