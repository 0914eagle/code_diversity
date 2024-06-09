
def get_votes(n_candidates, n_seats, n_citizens, n_voted, votes):
    # Initialize the votes dictionary
    votes_dict = {}
    for i in range(n_candidates):
        votes_dict[i + 1] = 0
    
    # Count the votes
    for i in range(n_voted):
        votes_dict[votes[i]] += 1
    
    # Sort the votes dictionary by value in descending order
    votes_sorted = sorted(votes_dict.items(), key=lambda x: x[1], reverse=True)
    
    # Initialize the seats dictionary
    seats_dict = {}
    for i in range(n_candidates):
        seats_dict[i + 1] = 0
    
    # Assign seats to candidates
    for i in range(n_seats):
        seats_dict[votes_sorted[i][0]] = 1
    
    # Return the seats dictionary
    return seats_dict

def get_chance(n_candidates, n_seats, n_citizens, n_voted, votes):
    # Get the votes
    votes_dict = get_votes(n_candidates, n_seats, n_citizens, n_voted, votes)
    
    # Initialize the chance dictionary
    chance_dict = {}
    for i in range(n_candidates):
        chance_dict[i + 1] = 0
    
    # Calculate the chance of each candidate
    for i in range(n_candidates):
        if votes_dict[i + 1] == votes_dict[i]:
            chance_dict[i + 1] = 2
        elif votes_dict[i + 1] > votes_dict[i]:
            chance_dict[i + 1] = 1
        else:
            chance_dict[i + 1] = 3
    
    # Return the chance dictionary
    return chance_dict

def get_result(n_candidates, n_seats, n_citizens, n_voted, votes):
    # Get the votes
    votes_dict = get_votes(n_candidates, n_seats, n_citizens, n_voted, votes)
    
    # Initialize the result dictionary
    result_dict = {}
    for i in range(n_candidates):
        result_dict[i + 1] = 0
    
    # Calculate the result of each candidate
    for i in range(n_candidates):
        if votes_dict[i + 1] == votes_dict[i]:
            result_dict[i + 1] = 3
        elif votes_dict[i + 1] > votes_dict[i]:
            result_dict[i + 1] = 1
        else:
            result_dict[i + 1] = 2
    
    # Return the result dictionary
    return result_dict

def main():
    # Read the input
    n_candidates, n_seats, n_citizens, n_voted = map(int, input().split())
    votes = list(map(int, input().split()))
    
    # Get the result
    result_dict = get_result(n_candidates, n_seats, n_citizens, n_voted, votes)
    
    # Print the result
    for i in range(n_candidates):
        print(result_dict[i + 1], end=" ")

if __name__ == '__main__':
    main()

