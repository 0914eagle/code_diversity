
def get_media_companies(sectors, teams, min_consecutive, min_distinct):
    # Initialize variables
    media_companies = 0
    team_colors = set()
    sector_colors = []
    consecutive_sectors = 0

    # Iterate through the sectors
    for sector in range(sectors):
        # Add the color of the current sector to the team colors set
        team_colors.add(teams[sector])

        # If the current sector has a color that is not in the team colors set, increment the consecutive sectors count
        if teams[sector] not in team_colors:
            consecutive_sectors += 1

        # If the consecutive sectors count is equal to the minimum required, increment the media companies count
        if consecutive_sectors == min_consecutive:
            media_companies += 1
            consecutive_sectors = 0
            team_colors = set()

    # Return the maximum number of media companies that can be sold broadcasting rights
    return media_companies

def get_minimum_distinct_colors(sectors, teams, min_consecutive, min_distinct):
    # Initialize variables
    team_colors = set()
    sector_colors = []
    consecutive_sectors = 0
    distinct_colors = 0

    # Iterate through the sectors
    for sector in range(sectors):
        # Add the color of the current sector to the team colors set
        team_colors.add(teams[sector])

        # If the current sector has a color that is not in the team colors set, increment the consecutive sectors count
        if teams[sector] not in team_colors:
            consecutive_sectors += 1

        # If the consecutive sectors count is equal to the minimum required, increment the distinct colors count
        if consecutive_sectors == min_consecutive:
            distinct_colors += 1
            consecutive_sectors = 0
            team_colors = set()

    # Return the minimum number of distinct colors required to satisfy the constraints
    return min_distinct - distinct_colors

if __name__ == '__main__':
    sectors, min_consecutive, min_distinct = map(int, input().split())
    teams = list(map(int, input().split()))
    media_companies = get_media_companies(sectors, teams, min_consecutive, min_distinct)
    minimum_distinct_colors = get_minimum_distinct_colors(sectors, teams, min_consecutive, min_distinct)
    print(media_companies)
    print(minimum_distinct_colors)

