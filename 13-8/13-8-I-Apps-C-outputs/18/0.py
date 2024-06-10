
def get_media_companies(sectors, min_consecutive_sectors, min_distinct_colors):
    # Initialize variables
    media_companies = 0
    current_sector = 1
    current_color = 1
    consecutive_sectors = 1
    distinct_colors = 1

    # Iterate through the sectors
    for sector in sectors:
        # If the current sector is the same as the previous sector, increment the consecutive sectors counter
        if sector == current_sector:
            consecutive_sectors += 1
        # If the current sector is different from the previous sector, reset the consecutive sectors counter
        else:
            consecutive_sectors = 1
        # Update the current sector and color
        current_sector = sector
        current_color = sector

        # If the current sector is the first sector or the previous sector is different from the current sector, increment the distinct colors counter
        if current_sector == 1 or sector != current_sector:
            distinct_colors += 1

        # If the consecutive sectors counter is greater than or equal to the minimum consecutive sectors required and the distinct colors counter is greater than or equal to the minimum distinct colors required, increment the media companies counter
        if consecutive_sectors >= min_consecutive_sectors and distinct_colors >= min_distinct_colors:
            media_companies += 1

    return media_companies

def main():
    sectors, min_consecutive_sectors, min_distinct_colors = map(int, input().split())
    sectors = list(map(int, input().split()))
    print(get_media_companies(sectors, min_consecutive_sectors, min_distinct_colors))

if __name__ == '__main__':
    main()

