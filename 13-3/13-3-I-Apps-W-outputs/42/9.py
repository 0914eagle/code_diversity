
def f1(N, M, chefs, emails):
    # Initialize a dictionary to store the votes for each country
    votes = {}

    # Iterate over the emails and increment the vote count for the corresponding country
    for email in emails:
        country = chefs[email]
        if country not in votes:
            votes[country] = 1
        else:
            votes[country] += 1

    # Find the country with the most votes
    max_votes = max(votes.values())
    country_winner = [country for country, votes in votes.items() if votes == max_votes][0]

    # Find the chef with the most votes from the country winner
    chef_winner = [chef for chef, country in chefs.items() if country == country_winner][0]

    return country_winner, chef_winner

def f2(N, M, chefs, emails):
    # Initialize a dictionary to store the votes for each chef
    votes = {}

    # Iterate over the emails and increment the vote count for the corresponding chef
    for email in emails:
        chef = chefs[email]
        if chef not in votes:
            votes[chef] = 1
        else:
            votes[chef] += 1

    # Find the chef with the most votes
    max_votes = max(votes.values())
    chef_winner = [chef for chef, votes in votes.items() if votes == max_votes][0]

    # Find the country of the chef winner
    country_winner = [country for chef, country in chefs.items() if chef == chef_winner][0]

    return country_winner, chef_winner

if __name__ == '__main__':
    N, M = map(int, input().split())
    chefs = {}
    for _ in range(N):
        chef, country = input().split()
        chefs[chef] = country
    emails = [input() for _ in range(M)]
    country_winner, chef_winner = f1(N, M, chefs, emails)
    print(country_winner)
    print(chef_winner)

