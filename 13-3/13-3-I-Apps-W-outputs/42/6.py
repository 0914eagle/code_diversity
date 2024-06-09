
def get_country_winner(chefs):
    country_votes = {}
    for chef in chefs:
        country = chef[1]
        if country not in country_votes:
            country_votes[country] = 1
        else:
            country_votes[country] += 1
    country_winner = max(country_votes, key=country_votes.get)
    return country_winner

def get_chef_winner(chefs, country_winner):
    chef_votes = {}
    for chef in chefs:
        if chef[1] == country_winner:
            name = chef[0]
            if name not in chef_votes:
                chef_votes[name] = 1
            else:
                chef_votes[name] += 1
    chef_winner = max(chef_votes, key=chef_votes.get)
    return chef_winner

def main():
    chefs = []
    with open("chefs.txt", "r") as f:
        for line in f:
            parts = line.strip().split()
            chefs.append((parts[0], parts[1]))
    country_winner = get_country_winner(chefs)
    chef_winner = get_chef_winner(chefs, country_winner)
    print(country_winner)
    print(chef_winner)

if __name__ == '__main__':
    main()

