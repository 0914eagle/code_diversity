
def get_country_winner(chef_country_list):
    country_votes = {}
    for chef, country in chef_country_list:
        if country not in country_votes:
            country_votes[country] = 1
        else:
            country_votes[country] += 1

    max_votes = max(country_votes.values())
    country_winner = [country for country, votes in country_votes.items() if votes == max_votes][0]

    return country_winner

def get_chef_winner(chef_country_list, country_winner):
    chef_votes = {}
    for chef, country in chef_country_list:
        if country == country_winner:
            if chef not in chef_votes:
                chef_votes[chef] = 1
            else:
                chef_votes[chef] += 1

    max_votes = max(chef_votes.values())
    chef_winner = [chef for chef, votes in chef_votes.items() if votes == max_votes][0]

    return chef_winner

def main():
    num_chefs, num_emails = map(int, input().split())
    chef_country_list = []
    for _ in range(num_chefs):
        chef, country = input().split()
        chef_country_list.append((chef, country))

    country_winner = get_country_winner(chef_country_list)
    chef_winner = get_chef_winner(chef_country_list, country_winner)

    print(country_winner)
    print(chef_winner)

if __name__ == '__main__':
    main()

