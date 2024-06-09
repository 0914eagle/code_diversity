
def get_country_winner(chef_votes):
    country_votes = {}
    for chef, country in chef_votes.items():
        if country not in country_votes:
            country_votes[country] = 1
        else:
            country_votes[country] += 1
    
    country_winner = None
    max_votes = 0
    for country, votes in country_votes.items():
        if votes > max_votes:
            max_votes = votes
            country_winner = country
        elif votes == max_votes and country < country_winner:
            country_winner = country
    
    return country_winner

def get_chef_winner(chef_votes):
    chef_winner = None
    max_votes = 0
    for chef, votes in chef_votes.items():
        if votes > max_votes:
            max_votes = votes
            chef_winner = chef
        elif votes == max_votes and chef < chef_winner:
            chef_winner = chef
    
    return chef_winner

def main():
    num_chefs, num_emails = map(int, input().split())
    chef_votes = {}
    for _ in range(num_chefs):
        chef, country = input().split()
        chef_votes[chef] = country
    
    for _ in range(num_emails):
        chef = input()
        if chef in chef_votes:
            country = chef_votes[chef]
            if country not in chef_votes:
                chef_votes[country] = 1
            else:
                chef_votes[country] += 1
    
    country_winner = get_country_winner(chef_votes)
    chef_winner = get_chef_winner(chef_votes)
    print(country_winner)
    print(chef_winner)

if __name__ == '__main__':
    main()

