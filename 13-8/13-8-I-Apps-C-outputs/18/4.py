
def get_maximum_media_companies(N, K, C, A):
    # Initialize variables
    media_companies = 0
    sector_colors = []
    consecutive_sectors = 0

    # Iterate through the sectors
    for i in range(N):
        # If the sector color is not in the list of sector colors, add it
        if A[i] not in sector_colors:
            sector_colors.append(A[i])
        # If the sector color is already in the list of sector colors, check if it forms a consecutive sector
        else:
            # If the sector color forms a consecutive sector, increment the consecutive sectors counter
            if A[i-1] == A[i]:
                consecutive_sectors += 1
            # If the sector color does not form a consecutive sector, reset the consecutive sectors counter
            else:
                consecutive_sectors = 0

        # If the consecutive sectors counter is equal to the minimum number of consecutive sectors required, increment the media companies counter
        if consecutive_sectors == K:
            media_companies += 1
            consecutive_sectors = 0

    # If the last sector color forms a consecutive sector, increment the media companies counter
    if consecutive_sectors == K:
        media_companies += 1

    return media_companies

def main():
    N, K, C = map(int, input().split())
    A = list(map(int, input().split()))
    print(get_maximum_media_companies(N, K, C, A))

if __name__ == '__main__':
    main()

