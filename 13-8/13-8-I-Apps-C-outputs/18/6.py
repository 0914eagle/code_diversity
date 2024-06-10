
def get_media_companies(num_sectors, min_consecutive_sectors, min_distinct_colors, team_assignments):
    # Initialize variables
    media_companies = 0
    sector_colors = []
    consecutive_sectors = 0

    # Iterate through the team assignments
    for i in range(num_sectors):
        # If the current sector has a different color than the previous sector, increase the consecutive sectors count
        if i == 0 or team_assignments[i] != team_assignments[i - 1]:
            consecutive_sectors += 1
        # If the consecutive sectors count is greater than or equal to the minimum required, increase the media companies count
        if consecutive_sectors >= min_consecutive_sectors:
            media_companies += 1
        # If the current sector has a different color than the previous sector, add the color to the sector colors list
        if i == 0 or team_assignments[i] != team_assignments[i - 1]:
            sector_colors.append(team_assignments[i])
        # If the number of distinct colors in the sector colors list is greater than or equal to the minimum required, return the media companies count
        if len(set(sector_colors)) >= min_distinct_colors:
            return media_companies

    # If the end of the list is reached and the media companies count is still less than the minimum required, return -1
    return -1

def main():
    num_sectors, min_consecutive_sectors, min_distinct_colors = map(int, input().split())
    team_assignments = list(map(int, input().split()))
    print(get_media_companies(num_sectors, min_consecutive_sectors, min_distinct_colors, team_assignments))

if __name__ == '__main__':
    main()

