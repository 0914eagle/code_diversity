
def expected_score(n, k):
    # Initialize a list to store the expected scores for each face
    expected_scores = [0] * (n + 1)
    
    # Base case: if we can only roll once, the expected score is the average of the faces
    if k == 1:
        return sum(range(1, n + 1)) / n
    
    # Recursive case: calculate the expected score for each face
    for face in range(1, n + 1):
        # Calculate the probability of rolling the current face
        prob = 1 / n
        
        # Calculate the expected score if we roll the current face
        expected_score_if_roll = face + expected_score(n, k - 1) * (1 - prob)
        
        # Calculate the expected score if we don't roll the current face
        expected_score_if_not_roll = expected_score(n, k - 1)
        
        # Add the expected scores for the current face to the list
        expected_scores[face] = expected_score_if_roll + expected_score_if_not_roll
    
    # Return the maximum expected score
    return max(expected_scores)

def main():
    n, k = map(int, input().split())
    print(expected_score(n, k))

if __name__ == '__main__':
    main()

