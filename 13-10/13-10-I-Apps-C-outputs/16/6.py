
def get_worst_rank(contests, scores):
    # Initialize the rank and points variables
    rank = 1
    points = 0
    
    # Loop through the contests and scores
    for i in range(len(contests)):
        # Check if the current contest is the final contest
        if i == len(contests) - 1:
            # Break the loop if it is the final contest
            break
        # Get the current contest's rank and points
        current_rank = contests[i]
        current_points = scores[i]
        # Check if the current points are valid
        if current_points > 0:
            # Add the current points to the total points
            points += current_points
            # Check if the current rank is higher than the current rank
            if current_rank > rank:
                # Update the rank with the current rank
                rank = current_rank
    
    # Return the worst possible rank
    return rank

def main():
    # Get the number of contests and participants
    n, m = map(int, input().split())
    # Create empty list to store the contests and scores
    contests = []
    scores = []
    
    # Loop through the participants
    for i in range(m):
        # Get the current participant's contests and scores
        contests_str, scores_str = input().split()
        # Convert the contests and scores to integers
        contests.append(list(map(int, contests_str.split())))
        scores.append(list(map(int, scores_str.split())))
    
    # Get the worst possible rank
    worst_rank = get_worst_rank(contests, scores)
    
    # Print the worst possible rank
    print(worst_rank)

if __name__ == '__main__':
    main()

