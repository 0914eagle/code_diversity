
def get_cutoff_score(a, b, c, d):
    # Calculate the total score of the participant on the 100th place
    total_score = a + c
    
    # Calculate the minimum number of participants needed to qualify to the final stage
    min_participants = (total_score // b) + 1
    
    # Calculate the minimum cutoff score
    cutoff_score = total_score - (min_participants - 1) * b
    
    return cutoff_score

