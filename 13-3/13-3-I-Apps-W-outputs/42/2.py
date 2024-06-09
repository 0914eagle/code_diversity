
def get_country_winner(chef_votes):
    country_votes = {}
    for chef, country in chef_votes.items():
        if country not in country_votes:
            country_votes[country] = 1
        else:
            country_votes[country] += 1

    country_winner = max(country_votes, key=country_votes.get)
    return country_winner

def get_chef_winner(chef_votes, country_winner):
    chef_votes_sorted = sorted(chef_votes.items(), key=lambda x: x[0])
    chef_winner = None
    max_votes = 0
    for chef, country in chef_votes_sorted:
        if country == country_winner:
            if chef_votes[chef] > max_votes:
                max_votes = chef_votes[chef]
                chef_winner = chef
            elif chef_votes[chef] == max_votes:
                if chef < chef_winner:
                    chef_winner = chef

    return chef_winner

def main():
    chef_votes = {}
    with open("chef_votes.txt", "r") as f:
        for line in f:
            line = line.strip().split()
            chef = line[0]
            country = line[1]
            if chef not in chef_votes:
                chef_votes[chef] = country
            else:
                print("Error: Duplicate chef found")
                return

    country_winner = get_country_winner(chef_votes)
    chef_winner = get_chef_winner(chef_votes, country_winner)

    print(country_winner)
    print(chef_winner)

if __name__ == '__main__':
    main()

