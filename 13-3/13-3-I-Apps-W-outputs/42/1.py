
def get_country_winner(chef_votes):
    # Initialize the country winner and its votes to the first country in the list
    country_winner = list(chef_votes.keys())[0]
    max_votes = chef_votes[country_winner]

    # Iterate over the remaining countries
    for country in list(chef_votes.keys())[1:]:
        # If the current country has more votes than the country winner, update the country winner
        if chef_votes[country] > max_votes:
            country_winner = country
            max_votes = chef_votes[country]

    return country_winner

def get_chef_winner(chef_votes, country_winner):
    # Initialize the chef winner and its votes to the first chef in the list
    chef_winner = list(chef_votes[country_winner].keys())[0]
    max_votes = chef_votes[country_winner][chef_winner]

    # Iterate over the remaining chefs
    for chef in list(chef_votes[country_winner].keys())[1:]:
        # If the current chef has more votes than the chef winner, update the chef winner
        if chef_votes[country_winner][chef] > max_votes:
            chef_winner = chef
            max_votes = chef_votes[country_winner][chef]

    return chef_winner

def main():
    # Read the input
    num_chefs, num_emails = map(int, input().split())
    chef_votes = {}
    for _ in range(num_chefs):
        chef, country = input().split()
        if country not in chef_votes:
            chef_votes[country] = {}
        chef_votes[country][chef] = 0
    for _ in range(num_emails):
        chef = input()
        country = list(chef_votes.keys())[0]
        for c in chef_votes:
            if chef in chef_votes[c]:
                country = c
                break
        chef_votes[country][chef] += 1

    # Get the country winner
    country_winner = get_country_winner(chef_votes)
    print(country_winner)

    # Get the chef winner
    chef_winner = get_chef_winner(chef_votes, country_winner)
    print(chef_winner)

if __name__ == '__main__':
    main()

