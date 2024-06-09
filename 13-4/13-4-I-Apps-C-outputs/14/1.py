
def get_election_results(n_candidates, n_seats, n_citizens, n_voted, votes):
    # Initialize the election results dictionary
    election_results = {}

    # Iterate over the votes and update the election results dictionary
    for i in range(n_voted):
        # Get the current vote
        vote = votes[i]

        # Check if the vote is already in the election results dictionary
        if vote not in election_results:
            # If not, add it to the dictionary with a count of 1
            election_results[vote] = 1
        else:
            # If it is, increment the count by 1
            election_results[vote] += 1

    # Sort the election results dictionary by value in descending order
    sorted_election_results = sorted(election_results.items(), key=lambda x: x[1], reverse=True)

    # Initialize the elected candidates list
    elected_candidates = []

    # Iterate over the sorted election results and add the top k candidates to the elected candidates list
    for i in range(n_seats):
        elected_candidates.append(sorted_election_results[i][0])

    # Initialize the remaining candidates list
    remaining_candidates = []

    # Iterate over the sorted election results and add the remaining candidates to the remaining candidates list
    for i in range(n_seats, n_candidates):
        remaining_candidates.append(sorted_election_results[i][0])

    # Initialize the output list
    output = []

    # Iterate over the elected candidates and set their output value to 1
    for candidate in elected_candidates:
        output.append(1)

    # Iterate over the remaining candidates and set their output value to 2 if they are in the elected candidates list, otherwise set it to 3
    for candidate in remaining_candidates:
        if candidate in elected_candidates:
            output.append(2)
        else:
            output.append(3)

    return output

def main():
    # Read the input from stdin
    n_candidates, n_seats, n_citizens, n_voted = map(int, input().split())
    votes = list(map(int, input().split()))

    # Call the get_election_results function and print the output
    print(*get_election_results(n_candidates, n_seats, n_citizens, n_voted, votes))

if __name__ == '__main__':
    main()

