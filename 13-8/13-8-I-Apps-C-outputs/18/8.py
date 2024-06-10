
def get_maximum_media_companies(number_of_sectors, minimum_consecutive_sectors, minimum_distinct_colors, teams):
    # Initialize a list to store the consecutive sectors for each media company
    media_companies = []
    # Iterate through the sectors
    for i in range(number_of_sectors):
        # If the sector is not part of any media company, create a new media company
        if i not in media_companies:
            media_company = [i]
            # Iterate through the remaining sectors
            for j in range(i+1, number_of_sectors):
                # If the sector is part of the current media company, add it to the list
                if teams[j] == teams[i]:
                    media_company.append(j)
            # If the media company has at least the minimum number of consecutive sectors and at least the minimum number of distinct colors, add it to the list of media companies
            if len(media_company) >= minimum_consecutive_sectors and len(set(teams[media_company])) >= minimum_distinct_colors:
                media_companies.append(media_company)
    # Return the maximum number of media companies that can be sold broadcasting rights
    return len(media_companies)

def main():
    number_of_sectors, minimum_consecutive_sectors, minimum_distinct_colors = map(int, input().split())
    teams = list(map(int, input().split()))
    print(get_maximum_media_companies(number_of_sectors, minimum_consecutive_sectors, minimum_distinct_colors, teams))

if __name__ == '__main__':
    main()

