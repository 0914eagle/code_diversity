
def get_country_winner(chef_votes):
    # Initialize the country winner and its votes to empty strings and 0
    country_winner = ""
    country_votes = 0
    
    # Iterate over the chef votes
    for chef, votes in chef_votes.items():
        # If the current chef has more votes than the current country winner
        if votes > country_votes:
            # Set the current chef as the new country winner
            country_winner = chef
            country_votes = votes
        # If the current chef has the same number of votes as the current country winner
        elif votes == country_votes:
            # Check if the current chef is lexicographically smaller than the current country winner
            if chef < country_winner:
                # Set the current chef as the new country winner
                country_winner = chef
                country_votes = votes
    
    return country_winner

def get_chef_winner(chef_votes):
    # Initialize the chef winner and its votes to empty strings and 0
    chef_winner = ""
    chef_votes = 0
    
    # Iterate over the chef votes
    for chef, votes in chef_votes.items():
        # If the current chef has more votes than the current chef winner
        if votes > chef_votes:
            # Set the current chef as the new chef winner
            chef_winner = chef
            chef_votes = votes
        # If the current chef has the same number of votes as the current chef winner
        elif votes == chef_votes:
            # Check if the current chef is lexicographically smaller than the current chef winner
            if chef < chef_winner:
                # Set the current chef as the new chef winner
                chef_winner = chef
                chef_votes = votes
    
    return chef_winner

def main():
    # Read the number of chefs and emails
    n, m = map(int, input().split())
    
    # Read the names of the chefs and their countries
    chef_countries = {}
    for _ in range(n):
        chef, country = input().split()
        chef_countries[chef] = country
    
    # Read the subjects of the emails
    emails = [input() for _ in range(m)]
    
    # Count the number of votes for each chef
    chef_votes = {}
    for email in emails:
        # Get the name of the chef from the email subject
        chef = email
        # If the chef is not in the dictionary, add them with 0 votes
        if chef not in chef_votes:
            chef_votes[chef] = 0
        # Increment the number of votes for the chef
        chef_votes[chef] += 1
    
    # Get the country winner
    country_winner = get_country_winner(chef_votes)
    # Get the chef winner
    chef_winner = get_chef_winner(chef_votes)
    
    # Print the country winner and the chef winner
    print(country_winner)
    print(chef_winner)

if __name__ == '__main__':
    main()

