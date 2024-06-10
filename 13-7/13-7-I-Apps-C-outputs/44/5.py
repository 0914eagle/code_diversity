
def get_rating(friends, matches):
    # Initialize the final rating of each friend to their initial rating
    rating = [friend for friend in friends]

    # Iterate over the matches
    for match in matches:
        # Get the indices of the friends playing in the match
        indices = [i for i, friend in enumerate(friends) if friend in match]

        # Sort the indices in descending order
        indices.sort(reverse=True)

        # Decrease the rating of the friends playing in the match
        for i in indices:
            rating[i] -= 1

    # Return the final rating of each friend
    return rating

def get_matches(friends):
    # Initialize the number of matches to 0
    matches = 0

    # Iterate over the friends
    for i, friend in enumerate(friends):
        # Get the indices of the friends who have a higher rating than the current friend
        indices = [i for i, rating in enumerate(friends) if rating > friend]

        # Add the number of matches needed to make the ratings equal
        matches += len(indices)

        # Decrease the rating of the current friend by the number of matches needed
        friends[i] -= matches

    # Return the number of matches needed
    return matches

def solve(friends):
    # Get the final rating of each friend
    rating = get_rating(friends, get_matches(friends))

    # Return the final rating and the number of matches needed
    return rating, get_matches(friends)

if __name__ == '__main__':
    n = int(input())
    friends = list(map(int, input().split()))
    rating, matches = solve(friends)
    print(rating)
    print(matches)
    for i in range(matches):
        print(''.join(['1' if j in friends else '0' for j in range(n)]))

