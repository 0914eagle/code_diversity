
def get_media_companies(n, k, c, teams):
    # Initialize a list to store the media companies and their constraints
    media_companies = []
    
    # Iterate over the teams and add them to the media companies if they satisfy the constraints
    for i in range(n):
        team = teams[i]
        if len(media_companies) == 0 or team != media_companies[-1][-1]:
            media_companies.append([team])
        else:
            media_companies[-1].append(team)
            if len(media_companies[-1]) == k:
                media_companies.append([])
    
    # Remove any empty lists from the media companies
    media_companies = [mc for mc in media_companies if mc]
    
    # Count the number of media companies that have at least c distinct colors
    num_media_companies = 0
    for mc in media_companies:
        colors = set()
        for team in mc:
            colors.add(team)
        if len(colors) >= c:
            num_media_companies += 1
    
    return num_media_companies

def main():
    n, k, c = map(int, input().split())
    teams = list(map(int, input().split()))
    print(get_media_companies(n, k, c, teams))

if __name__ == '__main__':
    main()

