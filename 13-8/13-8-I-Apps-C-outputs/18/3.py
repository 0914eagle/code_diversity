
def get_max_media_companies(n, k, c, teams):
    # Initialize a list to store the colors of the teams
    colors = []
    # Iterate over the teams and append the colors to the list
    for team in teams:
        if team not in colors:
            colors.append(team)
    # Sort the list of colors in descending order
    colors.sort(reverse=True)
    # Initialize a variable to store the maximum number of media companies
    max_media_companies = 0
    # Iterate over the teams and check if the conditions are met
    for i in range(len(teams)):
        # Check if the current team is the same as the previous team
        if i > 0 and teams[i] == teams[i - 1]:
            # If the current team is the same as the previous team, continue to the next iteration
            continue
        # Check if the current team has at least K consecutive sectors with the same color
        if teams[i] in teams[i:i + k]:
            # If the current team has at least K consecutive sectors with the same color, increment the maximum number of media companies
            max_media_companies += 1
        # Check if the current team has at least C distinct colors
        if len(set(teams[i:i + k])) >= c:
            # If the current team has at least C distinct colors, increment the maximum number of media companies
            max_media_companies += 1
    return max_media_companies

def main():
    n, k, c = map(int, input().split())
    teams = list(map(int, input().split()))
    print(get_max_media_companies(n, k, c, teams))

if __name__ == '__main__':
    main()

