
def get_min_cuts(poles, n):
    # Sort the poles in non-decreasing order
    poles.sort()
    # Initialize the minimum number of cuts as 0
    min_cuts = 0
    # Loop through the poles and check if they are long enough to be used as fence posts
    for i in range(len(poles)):
        if poles[i] >= n:
            # If a pole is long enough, remove it from the list and increment the minimum number of cuts
            poles.pop(i)
            min_cuts += 1
    # Return the minimum number of cuts needed to build the fence
    return min_cuts

def main():
    k, n = map(int, input().split())
    poles = list(map(int, input().split()))
    print(get_min_cuts(poles, n))

if __name__ == '__main__':
    main()

