
def count_can_ride(heights, K):
    count = 0
    for height in heights:
        if height >= K:
            count += 1
    return count

def main():
    N, K = map(int, input().split())
    heights = list(map(int, input().split()))
    print(count_can_ride(heights, K))

if __name__ == '__main__':
    main()

