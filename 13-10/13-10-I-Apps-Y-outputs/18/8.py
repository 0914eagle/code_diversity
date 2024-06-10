
def get_scores(target_score):
    # Initialize a list to store the scores
    scores = []
    
    # Iterate through the possible scores (1-20)
    for i in range(1, 21):
        # Check if the current score is a valid solution
        if i * 3 == target_score:
            # If it is, add it to the list of scores
            scores.append("triple " + str(i))
        elif i * 2 == target_score:
            # If it is, add it to the list of scores
            scores.append("double " + str(i))
        elif i == target_score:
            # If it is, add it to the list of scores
            scores.append("single " + str(i))
    
    # Return the list of scores
    return scores

def main():
    # Read the target score from stdin
    target_score = int(input())
    
    # Get the list of scores that add up to the target score
    scores = get_scores(target_score)
    
    # Print the scores
    for score in scores:
        print(score)

if __name__ == '__main__':
    main()

