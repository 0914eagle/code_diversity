
def get_throw_scores(target_score):
    # Initialize a list to store the throw scores
    throw_scores = []
    
    # Iterate through the possible throw scores
    for i in range(1, 21):
        # Check if the current throw score is less than or equal to the target score
        if i <= target_score:
            # Add the current throw score to the list
            throw_scores.append(i)
            # Subtract the current throw score from the target score
            target_score -= i
    
    # If the target score is not reached, return "impossible"
    if target_score > 0:
        return "impossible"
    
    # If the target score is reached, return the list of throw scores
    return throw_scores

def main():
    # Read a line of input from stdin and convert it to an integer
    target_score = int(input())
    
    # Call the get_throw_scores function and store the result in a variable
    throw_scores = get_throw_scores(target_score)
    
    # Check if the get_throw_scores function returned "impossible"
    if throw_scores == "impossible":
        # If it did, print "impossible"
        print("impossible")
    else:
        # If it didn't, iterate through the list of throw scores
        for i in range(len(throw_scores)):
            # Print the current throw score
            print(f"single {throw_scores[i]}")
            
            # If the current throw score is a multiple of 2, print "double"
            if throw_scores[i] % 2 == 0:
                print(f"double {throw_scores[i]}")
            
            # If the current throw score is a multiple of 3, print "triple"
            if throw_scores[i] % 3 == 0:
                print(f"triple {throw_scores[i]}")
                
if __name__ == '__main__':
    main()

