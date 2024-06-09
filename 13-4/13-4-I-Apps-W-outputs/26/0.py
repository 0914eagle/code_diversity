
def get_score(s, e, e_success, e_failure):
    # Initialize variables
    weight = 25
    score = 0
    
    # While there is still energy left and the weight is less than the maximum conceivable lift
    while e > 0 and weight < 225:
        # If the weight is greater than or equal to the strength
        if weight >= s:
            # Successful lift, decrease energy by e_success
            e -= e_success
            # Increase score by weight
            score += weight
        # If the weight is less than the strength
        else:
            # Failed lift, decrease energy by e_failure
            e -= e_failure
        # Increase weight by 25 kg
        weight += 25
    
    # Return the score
    return score

def get_d(e, e_success, e_failure):
    # Initialize variables
    d = 0
    s = 0
    
    # While the score is less than the strength
    while get_score(s, e, e_success, e_failure) < s:
        # Increase the strength by 1 kg
        s += 1
        # Increase the minimum weight by 1 kg
        d += 1
    
    # Return the minimum weight
    return d

if __name__ == '__main__':
    e, e_success, e_failure = map(int, input().split())
    print(get_d(e, e_success, e_failure))

