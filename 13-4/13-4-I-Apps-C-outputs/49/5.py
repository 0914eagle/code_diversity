
def get_min_cuts(poles, fence_length):
    # Sort the poles in descending order
    poles.sort(reverse=True)
    # Initialize variables to keep track of the cuts and the fence length
    cuts = 0
    fence_len = 0
    # Loop through the poles and add them to the fence until the fence is long enough
    for pole in poles:
        fence_len += pole
        cuts += 1
        if fence_len >= fence_length:
            break
    return cuts

def main():
    K, N = map(int, input().split())
    poles = list(map(int, input().split()))
    print(get_min_cuts(poles, N))

if __name__ == '__main__':
    main()

