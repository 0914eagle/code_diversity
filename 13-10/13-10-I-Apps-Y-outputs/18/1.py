
def get_throw_scores(target_score):
    # Initialize a list to store the throw scores
    throw_scores = []
    
    # Iterate through the possible values of d (1 to 20)
    for d in range(1, 21):
        # Check if the single score is equal to the target score
        if d == target_score:
            # Add the single score to the list of throw scores
            throw_scores.append(f"single {d}")
            # Return the list of throw scores
            return throw_scores
        # Check if the double score is equal to the target score
        elif 2 * d == target_score:
            # Add the double score to the list of throw scores
            throw_scores.append(f"double {d}")
            # Return the list of throw scores
            return throw_scores
        # Check if the triple score is equal to the target score
        elif 3 * d == target_score:
            # Add the triple score to the list of throw scores
            throw_scores.append(f"triple {d}")
            # Return the list of throw scores
            return throw_scores
    
    # If the target score cannot be achieved, return "impossible"
    return "impossible"

def main():
    # Read a line of input from stdin and convert it to an integer
    target_score = int(input().strip())
    
    # Call the get_throw_scores function and store the result in throw_scores
    throw_scores = get_throw_scores(target_score)
    
    # Print the list of throw scores
    for throw_score in throw_scores:
        print(throw_score)

if __name__ == '__main__':
    main()

