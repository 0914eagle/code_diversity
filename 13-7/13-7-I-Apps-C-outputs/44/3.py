
def get_equal_ratings(n, ratings):
    # Sort the ratings in descending order
    ratings.sort(reverse=True)
    # Initialize the final ratings and the number of matches
    final_ratings = [0] * n
    matches = 0
    # Loop through the ratings and form parties of size 2 to 5
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                for l in range(k+1, n):
                    # Check if the party has equal ratings
                    if ratings[i] == ratings[j] == ratings[k] == ratings[l]:
                        # Update the final ratings and the number of matches
                        final_ratings[i] += 1
                        final_ratings[j] += 1
                        final_ratings[k] += 1
                        final_ratings[l] += 1
                        matches += 1
                        break
    return final_ratings, matches

def get_parties(n, final_ratings, matches):
    # Initialize the parties and the current rating
    parties = []
    current_rating = 0
    # Loop through the final ratings and form parties
    for i in range(n):
        # Check if the current rating is equal to the final rating
        if current_rating == final_ratings[i]:
            # Add the current party to the list of parties
            parties.append([i])
            current_rating += 1
        # Check if the current rating is not equal to the final rating
        else:
            # Add the current party to the list of parties
            parties.append([i])
            current_rating += 1
            # Update the current rating
            current_rating = final_ratings[i]
    # Shuffle the parties to randomize the order
    import random
    random.shuffle(parties)
    # Initialize the list of matches
    match_list = []
    # Loop through the parties and form matches
    for party in parties:
        # Check if the party has two or more members
        if len(party) >= 2:
            # Add the party to the list of matches
            match_list.append(party)
    # Return the list of matches
    return match_list

def get_match_list(n, final_ratings, matches):
    # Get the list of parties
    party_list = get_parties(n, final_ratings, matches)
    # Initialize the list of matches
    match_list = []
    # Loop through the parties and form matches
    for party in party_list:
        # Check if the party has two or more members
        if len(party) >= 2:
            # Add the party to the list of matches
            match_list.append(party)
    # Return the list of matches
    return match_list

def get_match_output(match_list):
    # Initialize the output
    output = ""
    # Loop through the matches and form the output
    for match in match_list:
        # Add the match to the output
        output += "".join([str(int(i in match)) for i in range(len(match_list[0]))]) + "\n"
    # Return the output
    return output

def main():
    # Read the input
    n = int(input())
    ratings = list(map(int, input().split()))
    # Get the equal ratings and the number of matches
    final_ratings, matches = get_equal_ratings(n, ratings)
    # Get the list of matches
    match_list = get_match_list(n, final_ratings, matches)
    # Get the output
    output = get_match_output(match_list)
    # Print the output
    print(output)

if __name__ == '__main__':
    main()

